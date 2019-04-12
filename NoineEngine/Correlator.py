import numpy as np
import pandas as pd
import nltk
from multiprocessing import Pool
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


dat = pd.read_csv(".questions_rank.csv", encoding='latin1')
dat['Rank'].fillna(0, inplace=True)


# select a sample - results will improve without sampling in tf-idf caluculations, but due to
# Kaggle kernel memory limit we have to make a compromise here.
ids = range(len(dat))
sample = dat.loc[ids, :]
#sample.shape


def purify_string(html):
    return re.sub('(\r\n)+|\r+|\n+', " ", re.sub('<[^<]+?>', '', html))


corpus = sample.loc[:, 'Question'].apply(purify_string)


lem = WordNetLemmatizer()
def cond_tokenize(t):
    if t is None:
        return []
    else:
        return [lem.lemmatize(w.lower()) for w in word_tokenize(t)]

p = Pool(8)
tokens = list(p.imap(cond_tokenize, corpus))
p.close()


# stops = stopwords.words('english')
pure_tokens = [" ".join(sent) for sent in tokens]


vectorizer = TfidfVectorizer(min_df=1, max_features=2000, stop_words='english', ngram_range=[1, 1], sublinear_tf=True)
tfidf = vectorizer.fit_transform(pure_tokens)


# Compress using SVD
# -------------------- Hyper Parameter ----------------------
tsvd = TruncatedSVD(n_components=500)
transformed = tsvd.fit_transform(tfidf)

# calculate pairwise cosine distance
D = distance.pdist(transformed, 'cosine')

# hierarchical clustering - tree calculation
L = hierarchy.linkage(D)


# In[67]:


# mean distance between clusters
#np.mean(D)


# In[69]:


# split clusters by criterion. Here 0.71 is used as the inconsistency criterion. Adjust the
# number to change cluster sizes
cls = hierarchy.fcluster(L, 0.71, criterion='inconsistent')


# In[64]:


df_cls = pd.DataFrame({'Pos': selected_ids, 'Cluster': cls})

cnts = df_cls.groupby('Cluster').size().sort_values(ascending=False)
cnts.sort_values(ascending=False).head()


# In[58]:


# add clusters to question data
bc = pd.concat([sample, df_cls.set_index('Pos')], axis=1)

bc.head()


# In[ ]:


# calculate cluster stats
#stats = bc.groupby('Cluster')['Score'].describe().unstack()


# In[ ]:


#stats.sort_values('count', ascending=False).head(10)


# In[ ]:


'''plt.figure(figsize=(12, 8))
plt.hlines([0], xmin=0, xmax=np.max(stats['count']) + 5, alpha=0.5)
plt.vlines([1], ymin=0, ymax=np.max(stats['mean']) + 50, alpha=0.5)
plt.scatter(stats['count'], stats['mean'], alpha=0.3)
plt.title("cluster mean score vs cluster size")
plt.xlabel("cluster size")
plt.ylabel("mean score")
plt.show()'''


# ### Check if clusters make sense

# In[53]:


bc.loc[bc['Cluster'] == cnts.index[4]][['Score', 'Title', 'Body']]


# In[ ]:


#bc.loc[bc['Cluster'] == cnts.index[1]][['Score', 'Title', 'Body']]


# In[ ]:


#bc.loc[bc['Cluster'] == cnts.index[2]][['Score', 'Title', 'Body']]


# We can improve our clusters by increasing sample size, using entire dataset to calculate tf-idf, adjusting cluster splitting criterion, using non-exclusive clustering techniques etc.
# 
# Next steps:
# 
#  1. Use clusters and most significant words in questions to generate question tags automatically
#  2. Use an autoencoder to perform semantical hashing for better estimates of question relatedness
