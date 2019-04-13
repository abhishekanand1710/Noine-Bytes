import numpy as np
import pandas as pd
import nltk
#from multiprocessing import Pool
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import re
from itertools import chain
from collections import Counter
import pickle
import scipy.io as scio
from sklearn.decomposition import TruncatedSVD
import scipy.spatial.distance as distance
import scipy.cluster.hierarchy as hierarchy
from scipy.stats import pearsonr


def cluster(id, corr, reqRank):

    # Initial
    dat = pd.read_csv("../NoineEngine/Questions_Rank.csv", encoding='latin1')
    dat['Rank'].fillna(0, inplace=True)
    ids = range(len(dat))
    sample = dat.loc[ids, :]
    L = np.loadtxt('./Linkage.txt')

    # Next Question
    if corr:
        rel_wt = 0.8
    else:
        rel_wt = 0.95

    cls = hierarchy.fcluster(L, rel_wt, criterion='inconsistent')
    df_cls = pd.DataFrame({'Pos': ids, 'Cluster': cls})
    bc = pd.concat([sample, df_cls.set_index('Pos')], axis=1)
    
    for i in range(len(bc['Pos'])):
        row_id = bc.iloc[i, 0]
        row_rank = bc.iloc[i, 2]

        if row_id == id and row_rank == reqRank:
            return bc.iloc[i+1, 0]
    
    cnts = df_cls.groupby('Cluster').size().sort_values(ascending=False)
    print(bc.loc[bc['Cluster'] == cnts.index[1]][['ID', 'Questions', 'Rank', 'Cluster']])