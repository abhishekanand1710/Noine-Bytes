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


dat = pd.read_csv("./Questions_Rank.csv", encoding='latin1')
dat['Rank'].fillna(0, inplace=True)


# select a sample - results will improve without sampling in tf-idf caluculations, but due to
# Kaggle kernel memory limit we have to make a compromise here.
ids = range(len(dat))
sample = dat.loc[ids, :]
#sample.shape


def purify_string(html):
    return re.sub('(\r\n)+|\r+|\n+', " ", re.sub('<[^<]+?>', '', html))


corpus = sample.loc[:, 'Questions'].apply(purify_string)


lem = WordNetLemmatizer()
def cond_tokenize(t):
    if t is None:
        return []
    else:
        return [lem.lemmatize(w.lower()) for w in word_tokenize(t)]

#p = Pool(8)
tokens = list(map(cond_tokenize, corpus))
#p.close()


# stops = stopwords.words('english')
pure_tokens = [" ".join(sent) for sent in tokens]


vectorizer = TfidfVectorizer(min_df=1, max_features=500, stop_words='english', ngram_range=[1, 1], sublinear_tf=True)
tfidf = vectorizer.fit_transform(pure_tokens)


# Compress using SVD
# -------------------- Hyper Parameter ----------------------
tsvd = TruncatedSVD(n_components=100)
transformed = tsvd.fit_transform(tfidf)

# calculate pairwise cosine distance
D = distance.pdist(transformed, 'cosine')

# hierarchical clustering - tree calculation
L = hierarchy.linkage(D)

np.savetxt('./Linkage.txt', L)

L = np.loadtxt('./Linkage.txt')

    # split clusters by criterion. Here 0.71 is used as the inconsistency criterion. Adjust the
    # number to change cluster sizes
cls = hierarchy.fcluster(L, 0.95, criterion='inconsistent')

df_cls = pd.DataFrame({'Pos': ids, 'Cluster': cls})

cnts = df_cls.groupby('Cluster').size().sort_values(ascending=False)

print(cnts.mean())
    # add clusters to question data
bc = pd.concat([sample, df_cls.set_index('Pos')], axis=1)

print(bc.loc[bc['Cluster'] == cnts.index[1]][['ID', 'Questions', 'Rank', 'Cluster']])