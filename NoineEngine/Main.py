
# This Script is run by Cloud function on new dataset upload
from Question_Ranker import ranker_tagger
from Correlator_Setup import setCorrelation

def main():
    ranker_tagger()
    setCorrelation()

main()
