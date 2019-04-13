import pandas as pd

def recommend(id):

    tags = []
    dat = pd.read_csv("../NoineEngine/Questions_Rank.csv", encoding='latin1')
    for i in range(len(dat['ID'])):
        if id == dat.iloc[i, 0]:
            tags = dat.iloc[i, 3].split(',')

    res = pd.read_csv("../NoineEngine/Resources.csv", encoding='latin1')
    for i in range(len(res['Links'])):
        for j in tags:
            if j == res.iloc[i, 1]:
                return res.iloc[i,0];
