# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir())


# Any results you write to the current directory are saved as output.
#!/usr/bin/env python

import nltk
# nltk.download()

import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


lmtzr = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

with open('./questions.txt', 'rb') as f:
     data = [l.decode('utf8', 'ignore') for l in f.readlines()]

questions = data.copy()

#print(data)

data_np = []


"""REMOVE PUNCTUATION"""
exclude = set(string.punctuation)
data_np = [ch for ch in data if ch not in exclude]

#print(data_np)

"""////////////////////////////////////////////////////////////////"""

"""TOCKENIZE & LEMMATIZE DATA"""

data_lemmatized=[]
data_tockenized=list()

for d in data_np:
    data_tockenized.append(word_tokenize(d))
# print(data_tockenized)
    
for ques in data_tockenized:
    temp_lem = []
    for word in ques:
        temp_lem.append(lmtzr.lemmatize(word))
    data_lemmatized.append(temp_lem)
    
# print(data_lemmatized)
# print(questions)

"""////////////////////////////////////////////////////////////////"""
"""REMOVE COMMONT WORDS AND LOWERCASE"""
filtered_sentences = []

for d_lem in data_lemmatized:
    temp_filter = []
    for w in d_lem:
        if w not in stop_words:
            temp_filter.append(w)
    filtered_sentences.append(temp_filter)

#filtered_sentence = [w for w in data_lemmatized if not w in stop_words]

#print(filtered_sentence)

all_words = []
for sent in filtered_sentences:
    temp_all = []
    for word in sent:
        temp_all.append(word.lower())
    all_words.append(temp_all)
        
    
# print(all_words)

for index, alw in enumerate(all_words):
    all_words[index] = nltk.FreqDist(alw)
    



"""////////////////////////////////////////////////////////////////"""

# file = open('./results.html','w')




"""CALCULATE WORD FREQUENCIES for lvl 1"""
# print("Bloolm's taxonomy for level 1")

l1 = []
know = []
for al in all_words:
    write_frequecny =(al["write"])
    list_frequency =(al["list"])
    label_frequency =(al["label"])
    name_frequency =(al["name"])
    state_frequency = (al["state"])
    define_frequency = (al["which"])
    knowledge_frequency1 = write_frequecny + list_frequency + label_frequency + name_frequency + state_frequency +define_frequency
    know.append(knowledge_frequency1)


com = []
for al in all_words:
    explain_frequency =(al["explain"])
    summarize_frequency =(al["category"])
    paraphrase_frequency =(al["paraphrase"])
    describe_frequency =(al["describe"])
    illustrate_frequency = (al["illustrate"])
    comprehension_frequency1 = explain_frequency + summarize_frequency + paraphrase_frequency + describe_frequency + illustrate_frequency
    com.append(comprehension_frequency1)


app = []
for al in all_words:
    use_frequcny =(al["use"])
    compute_frequency =(al["compute"])
    solve_frequency =(al["solve"])
    demonstrate_frequency =(al["demonstrate"])
    apply_frequency = (al["apply"])
    construct_frequency = (al["construct"])
    application_frequency1 = use_frequcny + compute_frequency + solve_frequency + demonstrate_frequency + apply_frequency +construct_frequency
    app.append(application_frequency1)



ana = []
for al in all_words:
    analyze_frequcny =(al["analyze"])
    categorize_frequency =(al["categorize"])
    compare_frequency =(al["compare"])
    contrast_frequency =(al["contrast"])
    separate_frequency = (al["separate"])
    analysis_frequency1 = analyze_frequcny + categorize_frequency + compare_frequency + contrast_frequency + separate_frequency
    ana.append(analysis_frequency1)



syn = []
for al in all_words:
    create_frequcny =(al["create"])
    design_frequency =(al["design"])
    hypothesize_frequency =(al["hypothesize"])
    invent_frequency =(al["invent"])
    develop_frequency = (al["develop"])
    synthesis_frequency1 = create_frequcny + design_frequency + hypothesize_frequency + invent_frequency + develop_frequency
    syn.append(synthesis_frequency1)
    


eva = []
for al in all_words:
    judge_frequcny =(al["judge"])
    recommend_frequency =(al["recommend"])
    critique_frequency =(al["critique"])
    justify_frequency =(al["justify"])
    evaluation_frequency1 = judge_frequcny + recommend_frequency + critique_frequency + justify_frequency
    eva.append(evaluation_frequency1)
    
l1.append(know)
l1.append(com)
l1.append(app)
l1.append(ana)
l1.append(syn)
l1.append(eva)


"""////////////////////////////////////////////////////////////////"""


# col2 = """</div>
# <div class="col-sm">"""
# print(col2)

"""CALCULATE WORD FREQUENCIES for lvl 2"""
# print("<h3> Bloolm's taxonomy for level 2 </h3>")

l2 = []
know = []

for al in all_words:
    select_freq =(al["select"])
    outline_freq =(al["outline"])
    write_freq=(al["write"])
    list_freq =(al["list"])
    recite_freq =(al["recite"])
    state_freq =(al["state"])
    name_freq =(al["name"])
    repeat_freq =(al["repeat"])
    identify_freq =(al["identify"])
    locate_freq =(al["locate"])
    label_frequ =(al["label"])
    draw_freq =(al["draw"])
    record_freq =(al["record"])
    knowledge_frequency2 = select_freq + outline_freq + write_freq + list_freq + recite_freq + state_freq + name_freq + repeat_freq + identify_freq + locate_freq + label_frequ + draw_freq + record_freq
    know.append(knowledge_frequency2)

com = []

for al in all_words:
    explain_freq =(al["explain"])
    describe_freq =(al["describe"])
    relate_freq =(al["relate"])
    estimate_freq =(al["estimate"])
    paraphrase_freq =(al["paraphrase"])
    confirm_freq =(al["confirm"])
    convert_freq =(al["convert"])
    match_freq =(al["match"])
    compare_freq =(al["compare"])
    discuss_freq =(al["discuss"])
    predict_freq =(al["predict"])
    infer_freq =(al["infer"])
    comprehension_frequency2 = explain_freq + describe_freq + relate_freq + estimate_freq + paraphrase_freq + confirm_freq + convert_freq + match_freq + compare_freq + discuss_freq + predict_freq + infer_freq
    com.append(comprehension_frequency2)

app = []

for al in all_words:
    construct_freq = (al["construct"])
    apply_freq = (al["apply"])
    modify_freq = (al["modify"])
    build_freq = (al["build"])
    prioritize_freq = (al["prioritize"])
    report_freq = (al["report"])
    sketch_freq = (al["sketch"])
    produce_freq = (al["produce"])
    application_frequency2 = construct_freq + apply_freq + modify_freq + build_freq + prioritize_freq + report_freq + sketch_freq + produce_freq
    app.append(application_frequency2)

ana = []

for al in all_words:
    analyze_freq =(al["analyze"])
    categorize_freq =(al["categorize"])
    compare_freq=(al["compare"])
    sort_freq = (al["sort"])
    investigate_freq = (al["investigate"])
    debate_freq = (al["debate"])
    differentiate_freq = (al["differentiate"])
    examine_freq = (al["examine"])
    analysis_frequency2 = analyze_freq + categorize_freq + compare_freq + sort_freq + investigate_freq + debate_freq +differentiate_freq + examine_freq
    ana.append(analysis_frequency2)

syn = []

for al in all_words:
    compose_freq =(al["compose"])
    combine_freq = (al["combine"])
    design_freq =(al["design"])
    generate_freq = (al["generate"])
    hypothesize_freq =(al["hypothesize"])
    formulate_freq = (al["formulate"])
    originate_freq = (al["originate"])
    invent_freq =(al["invent"])
    revise_frequency = (al["revise"])
    synthesis_frequency2 = compose_freq + combine_freq + design_freq + generate_freq + hypothesize_freq + formulate_freq +originate_freq + invent_freq +revise_frequency
    syn.append(synthesis_frequency2)

eva = []

for al in all_words:
    judge_freq=(al["judge"])
    justify_frequency =(al["justify"])
    conclude_freq = (al["conclude"])
    prioritize_freq = (al["prioritize"])
    rate_freq = (al["rate"])
    criticize_freq = (al["criticize"])
    assess_freq = (al["assess"])
    appraise_freq = (al["appraise"])
    critique_freq = (al["critique"])
    evaluation_frequency2 = judge_freq + justify_frequency + conclude_freq + prioritize_freq + rate_freq + criticize_freq + assess_freq + appraise_freq + critique_freq
    eva.append(evaluation_frequency2)


l2.append(know)
l2.append(com)
l2.append(app)
l2.append(ana)
l2.append(syn)
l2.append(eva)

# print("<hr><br><br><br>")
# """////////////////////////////////////////////////////////////////"""
# col3 = """</div>
# <div class="col-sm">"""
# print(col3)


"""CALCULATE WORD FREQUENCIES for WIKIPEDIA diagram"""
# print("<h3> Bloolm's taxonomy for WIKI </h3>")
# print("<hr><br>")

l3 = []

know = []

for al in all_words:
    select_freq =(al["select"])
    list_freq =(al["list"])
    name_freq =(al["name"])
    define_freq =(al["define"])
    describe_freq=(al["describe"])
    memorize_freq =(al["memorize"])
    label_freq =(al["label"])
    identify_freq =(al["identify"])
    locate_freq =(al["locate"])
    recite_freq =(al["recite"])
    state_freq =(al["state"])
    recognize_freq =(al["recognize"])
    knowledge_frequency_wiki = select_freq + list_freq + name_freq + define_freq + describe_freq + memorize_freq + label_freq + identify_freq + locate_freq + recite_freq + state_freq + recognize_freq
    know.append(knowledge_frequency_wiki)

com = []

for al in all_words:
    match_freq =(al["match"])
    restate_freq = (al["restate"])
    paraphrase_freq =(al["paraphrase"])
    rewrite_freq = (al["rewrite"])
    example_freq = (al["example"])
    express_freq = (al["express"])
    illustrate_freq = (al["illustrate"])
    explain_freq =(al["explain"])
    defend_freq = (al["defend"])
    distinguish_freq = (al["distinguish"])
    summarize_freq = (al["summarize"])
    interrelate_freq = (al["interrelate"])
    interpret_freq = (al["interpret"])
    extend_freq = (al["extend"])
    comprehension_frequency_wiki = match_freq + restate_freq + paraphrase_freq + rewrite_freq + example_freq + express_freq + explain_freq + defend_freq + distinguish_freq + summarize_freq + interrelate_freq + interpret_freq + extend_freq
    com.append(comprehension_frequency_wiki)


app = []

for al in all_words:
    organize_freq = (al["organize"])
    organize_freq = (al["organize"])
    generalize_freq = (al["generalize"])
    dramatize_freq = (al["dramatize"])
    prepare_freq = (al["prepare"])
    produce_freq = (al["produce"])
    choose_freq = (al["choose"])
    sketch_freq = (al["sketch"])
    apply_freq = (al["apply"])
    solve_freq = (al["solve"])
    draw_freq = (al["draw"])
    show_freq = (al["show"])
    paint_freq = (al["paint"])
    application_frequency_wiki = organize_freq + generalize_freq + dramatize_freq + prepare_freq + produce_freq + choose_freq + sketch_freq + apply_freq + solve_freq + draw_freq + show_freq + paint_freq
    app.append(application_frequency_wiki)

ana = []

for al in all_words:
    compare_freq=(al["compare"])
    analyze_freq =(al["analyze"])
    classify_freq = (al["classify"])
    pointout_freq = (al["point"])
    distinguish_freq = (al["distinguish"])
    categorize_freq = (al["categorize"])
    differentiate_freq = (al["differentiate"])
    subdivide_freq = (al["subdivide"])
    infer_freq = (al["infer"])
    survey_freq = (al["survey"])
    select_freq = (al["select"])
    prioritize_freq = (al["prioritize"])
    analysis_frequency_wiki = compare_freq + analyze_frequcny + classify_freq + pointout_freq + distinguish_freq + categorize_freq + differentiate_freq + subdivide_freq + infer_freq + survey_freq + select_freq + prioritize_freq
    ana.append(analysis_frequency_wiki)

syn = []

for al in all_words:
    compose_freq =(al["compose"])
    originate_freq = (al["originate"])
    hypothesize_freq =(al["hypothesize"])
    develop_freq = (al["develop"])
    design_freq =(al["design"])
    combine_freq = (al["combine"])
    construct_freq = (al["construct"])
    produce_freq = (al["produce"])
    plan_freq = (al["plan"])
    create_freq = (al["create"])
    invent_freq =(al["invent"])
    organize_freq = (al["organize"])
    synthesis_frequency_wiki = compose_freq + originate_freq + hypothesize_freq + develop_freq + design_freq + combine_freq + construct_freq + produce_freq + plan_freq + create_freq + invent_freq + organize_freq
    syn.append(synthesis_frequency_wiki)

eva = []

for al in all_words:
    judge_freq=(al["judge"])
    relate_freq = (al["relate"])
    weight_freq = (al["weight"])
    criticize_freq = (al["criticize"])
    support_freq = (al["support"])
    criticize_freq = (al["criticize"])
    support_freq = (al["support"])
    evaluate_freq = (al["evaluate"])
    consider_freq = (al["consider"])
    critique_freq = (al["critique"])
    recommend_freq = (al["recommend"])
    summarize_freq = (al["summarize"])
    appraise_freq = (al["appraise"])
    compare_freq = (al["compare"])
    evaluation_frequency_wiki = judge_freq + relate_freq + weight_freq + criticize_freq + support_freq + evaluate_freq + consider_freq + critique_freq + recommend_freq + summarize_freq + appraise_freq + compare_freq
    eva.append(evaluation_frequency_wiki)



l3.append(know)
l3.append(com)
l3.append(app)
l3.append(ana)
l3.append(syn)
l3.append(eva)


import numpy as np

s1 = np.zeros(len(questions))
s2 = np.zeros(len(questions))
s3 = np.zeros(len(questions))

for l in l1:
    for i in range(len(questions)):
        s1[i] = s1[i] + l[i]
    
for l in l2:
    for i in range(len(questions)):
        s2[i] = s2[i] + l[i]

for l in l3:
    for i in range(len(questions)):
        s3[i] = s3[i] + l[i]


def get_rank(a, b, c):
    if a>b:
        if a>c:
            return 1
        else:
            return 3
    elif b>c:
        return 2
    else:
        return 3
            

ranks = []
for a, b, c in zip(s1, s2, s3):
    ranks.append(get_rank(a, b, c))

# print(ranks)



import re
import pandas as pd
stemmer = nltk.stem.PorterStemmer()
f = open("AutoTagger.txt", "r")
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
    return ",".join(finalTags)


for index, q in enumerate(questions):
    questions[index] = re.sub(r'[\n\r\t]', '', q)

idx = 0

ranked_questions = []

for ques, rank in zip(questions, ranks):
    tags = autoTagger(ques)    
    ranked_questions.append([idx, ques, rank, tags])
    idx += 1
    
# print(ranked_questions)

question_df = pd.DataFrame(ranked_questions, columns = ['ID', 'Questions', 'Rank', 'Tags']) 
print(question_df)

question_df.to_csv('Questions_Rank.csv', index=False)
    


"""////////////////////////////////////////////////////////////////"""
