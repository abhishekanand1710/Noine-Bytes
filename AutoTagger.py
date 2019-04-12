import string
import nltk # for text preprocessing
stemmer = nltk.stem.PorterStemmer()
f = open("../input/AutoTagger.txt", "r")
unique_all_tags = f.read().splitlines()
def autoTagger(question):
    finalTags = []
    exclude = set(string.punctuation)
    for word in question.split(" "):
        word_nopunc = []
        for i,ch in enumerate(word):
            if ch not in exclude and type(ch) == str:
                word_nopunc.append(ch)
        word_nopunc = "".join(word_nopunc)
        word_stem = stemmer.stem(word_nopunc)
        if word_stem in unique_all_tags:
            finalTags.append(word_nopunc)
    return finalTags
