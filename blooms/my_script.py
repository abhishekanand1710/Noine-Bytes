#!/usr/bin/env python

import nltk
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


lmtzr = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

with open('./math.txt', 'rb') as f:
     data = [l.decode('utf8', 'ignore') for l in f.readlines()]



data_lemmatized=[]
data_tockenized=[]

"""REMOVE PUNCTUATION"""
exclude = set(string.punctuation)
data_np = ''.join(ch for ch in data if ch not in exclude)

"""////////////////////////////////////////////////////////////////"""

"""TOCKENIZE & LEMMATIZE DATA"""

data_tockenized= word_tokenize(data_np)

for word in data_tockenized:
    data_lemmatized.append(lmtzr.lemmatize(word))

"""////////////////////////////////////////////////////////////////"""
"""REMOVE COMMONT WORDS AND LOWERCASE"""
filtered_sentence = [w for w in data_lemmatized if not w in stop_words]

all_words = []
for word in filtered_sentence:
    all_words.append(word.lower())

all_words = nltk.FreqDist(all_words)

"""////////////////////////////////////////////////////////////////"""

file = open('./views/results.html','w')

top = """
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Bloom's taxonomy tool</title>
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.3/angular.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/angular.js/1.3.3/angular-route.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
<script src="script.js"></script>
</head>
<body>
  <div class="container-fluid">
<div>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">Bloom's taxonomy tool</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="#">home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/about">about</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/contact">contact</a>
        </li>
      </ul>
    </div>
  </nav>
</div>
<br/>
<div class="jumbotron">
<div class="container">
<div class="row">
<div class="col-sm">
"""

file.write(top)



"""CALCULATE WORD FREQUENCIES for lvl 1"""
file.write("<h3> Bloolm's taxonomy for level 1 </h3>")
file.write("<hr><br>")

write_frequecny =(all_words["write"])
list_frequency =(all_words["list"])
label_frequency =(all_words["label"])
name_frequency =(all_words["name"])
state_frequency = (all_words["state"])
define_frequency = (all_words["define"])



knowledge_frequency1 = write_frequecny + list_frequency + label_frequency + name_frequency + state_frequency +define_frequency


file.write("<p><b>Knowledge</b> repeated: "+str(knowledge_frequency1)+" times</p>")


explain_frequency =(all_words["explain"])
summarize_frequency =(all_words["summarize"])
paraphrase_frequency =(all_words["paraphrase"])
describe_frequency =(all_words["describe"])
illustrate_frequency = (all_words["illustrate"])



comprehension_frequency1 = explain_frequency + summarize_frequency + paraphrase_frequency + describe_frequency + illustrate_frequency


file.write("<p><b>Comprehension</b> repeated: "+str(comprehension_frequency1)+" times</p>")

use_frequcny =(all_words["use"])
compute_frequency =(all_words["compute"])
solve_frequency =(all_words["solve"])
demonstrate_frequency =(all_words["demonstrate"])
apply_frequency = (all_words["apply"])
construct_frequency = (all_words["construct"])



application_frequency1 = use_frequcny + compute_frequency + solve_frequency + demonstrate_frequency + apply_frequency +construct_frequency


file.write("<p><b>Application</b> repeated: "+str(application_frequency1)+" times</p>")



analyze_frequcny =(all_words["analyze"])
categorize_frequency =(all_words["categorize"])
compare_frequency =(all_words["compare"])
contrast_frequency =(all_words["contrast"])
separate_frequency = (all_words["separate"])

analysis_frequency1 = analyze_frequcny + categorize_frequency + compare_frequency + contrast_frequency + separate_frequency


file.write("<p> <b>Analysis</b> repeated: "+str(analysis_frequency1)+" times</p>")

create_frequcny =(all_words["create"])
design_frequency =(all_words["design"])
hypothesize_frequency =(all_words["hypothesize"])
invent_frequency =(all_words["invent"])
develop_frequency = (all_words["develop"])

synthesis_frequency1 = create_frequcny + design_frequency + hypothesize_frequency + invent_frequency + develop_frequency


file.write("<p><b>Synthesis</b> repeated: "+str(synthesis_frequency1)+" times</p>")

judge_frequcny =(all_words["judge"])
recommend_frequency =(all_words["recommend"])
critique_frequency =(all_words["critique"])
justify_frequency =(all_words["justify"])


evaluation_frequency1 = judge_frequcny + recommend_frequency + critique_frequency + justify_frequency


file.write("<p><b>Evaluation</b> repeated: "+str(evaluation_frequency1)+" times</p>")
file.write("<hr><br><br><br>")
"""////////////////////////////////////////////////////////////////"""


col2 = """</div>
<div class="col-sm">"""
file.write(col2)

"""CALCULATE WORD FREQUENCIES for lvl 2"""
file.write("<h3> Bloolm's taxonomy for level 2 </h3>")
file.write("<hr><br>")



select_freq =(all_words["select"])
outline_freq =(all_words["outline"])
write_freq=(all_words["write"])
list_freq =(all_words["list"])
recite_freq =(all_words["recite"])
state_freq =(all_words["state"])
name_freq =(all_words["name"])
repeat_freq =(all_words["repeat"])
identify_freq =(all_words["identify"])
locate_freq =(all_words["locate"])
label_frequ =(all_words["label"])
draw_freq =(all_words["draw"])
record_freq =(all_words["record"])


knowledge_frequency2 = select_freq + outline_freq + write_freq + list_freq + recite_freq + state_freq + name_freq + repeat_freq + identify_freq + locate_freq + label_frequ + draw_freq + record_freq


file.write("<p><b>Knowledge</b> repeated: "+str(knowledge_frequency2)+" times</p>")

explain_freq =(all_words["explain"])
describe_freq =(all_words["describe"])
relate_freq =(all_words["relate"])
estimate_freq =(all_words["estimate"])
paraphrase_freq =(all_words["paraphrase"])
confirm_freq =(all_words["confirm"])
convert_freq =(all_words["convert"])
match_freq =(all_words["match"])
compare_freq =(all_words["compare"])
discuss_freq =(all_words["discuss"])
predict_freq =(all_words["predict"])
infer_freq =(all_words["infer"])

comprehension_frequency2 = explain_freq + describe_freq + relate_freq + estimate_freq + paraphrase_freq + confirm_freq + convert_freq + match_freq + compare_freq + discuss_freq + predict_freq + infer_freq


file.write("<p><b>Comprehension</b> repeated: "+str(comprehension_frequency2)+" times</p>")

construct_freq = (all_words["construct"])
apply_freq = (all_words["apply"])
modify_freq = (all_words["modify"])
build_freq = (all_words["build"])
prioritize_freq = (all_words["prioritize"])
report_freq = (all_words["report"])
sketch_freq = (all_words["sketch"])
produce_freq = (all_words["produce"])

application_frequency2 = construct_freq + apply_freq + modify_freq + build_freq + prioritize_freq + report_freq + sketch_freq + produce_freq


file.write("<p><b>Application</b> repeated: "+str(application_frequency2)+" times</p>")

analyze_freq =(all_words["analyze"])
categorize_freq =(all_words["categorize"])
compare_freq=(all_words["compare"])
sort_freq = (all_words["sort"])
investigate_freq = (all_words["investigate"])
debate_freq = (all_words["debate"])
differentiate_freq = (all_words["differentiate"])
examine_freq = (all_words["examine"])

analysis_frequency2 = analyze_freq + categorize_freq + compare_freq + sort_freq + investigate_freq + debate_freq +differentiate_freq + examine_freq


file.write("<p><b>Analysis</b> repeated: "+str(analysis_frequency2)+" times</p>")

compose_freq =(all_words["compose"])
combine_freq = (all_words["combine"])
design_freq =(all_words["design"])
generate_freq = (all_words["generate"])
hypothesize_freq =(all_words["hypothesize"])
formulate_freq = (all_words["formulate"])
originate_freq = (all_words["originate"])
invent_freq =(all_words["invent"])
revise_frequency = (all_words["revise"])

synthesis_frequency2 = compose_freq + combine_freq + design_freq + generate_freq + hypothesize_freq + formulate_freq +originate_freq + invent_freq +revise_frequency


file.write("<p><b>Synthesis</b> repeated: "+str(synthesis_frequency2)+" times</p>")

judge_freq=(all_words["judge"])
justify_frequency =(all_words["justify"])
conclude_freq = (all_words["conclude"])
prioritize_freq = (all_words["prioritize"])
rate_freq = (all_words["rate"])
criticize_freq = (all_words["criticize"])
assess_freq = (all_words["assess"])
appraise_freq = (all_words["appraise"])
critique_freq = (all_words["critique"])

evaluation_frequency2 = judge_freq + justify_frequency + conclude_freq + prioritize_freq + rate_freq + criticize_freq + assess_freq + appraise_freq + critique_freq


file.write("<p><b>Evaluation</b> repeated: "+str(evaluation_frequency2)+" times</p>")
file.write("<hr><br><br><br>")
"""////////////////////////////////////////////////////////////////"""
col3 = """</div>
<div class="col-sm">"""
file.write(col3)


"""CALCULATE WORD FREQUENCIES for WIKIPEDIA diagram"""
file.write("<h3> Bloolm's taxonomy for WIKI </h3>")
file.write("<hr><br>")


select_freq =(all_words["select"])
list_freq =(all_words["list"])
name_freq =(all_words["name"])
define_freq =(all_words["define"])
describe_freq=(all_words["describe"])
memorize_freq =(all_words["memorize"])
label_freq =(all_words["label"])
identify_freq =(all_words["identify"])
locate_freq =(all_words["locate"])
recite_freq =(all_words["recite"])
state_freq =(all_words["state"])
recognize_freq =(all_words["recognize"])


knowledge_frequency_wiki = select_freq + list_freq + name_freq + define_freq + describe_freq + memorize_freq + label_freq + identify_freq + locate_freq + recite_freq + state_freq + recognize_freq


file.write("<p><b>Knowledge</b> repeated: "+str(knowledge_frequency_wiki)+" times</p>")



match_freq =(all_words["match"])
restate_freq = (all_words["restate"])
paraphrase_freq =(all_words["paraphrase"])
rewrite_freq = (all_words["rewrite"])
example_freq = (all_words["example"])
express_freq = (all_words["express"])
illustrate_freq = (all_words["illustrate"])
explain_freq =(all_words["explain"])
defend_freq = (all_words["defend"])
distinguish_freq = (all_words["distinguish"])
summarize_freq = (all_words["summarize"])
interrelate_freq = (all_words["interrelate"])
interpret_freq = (all_words["interpret"])
extend_freq = (all_words["extend"])



comprehension_frequency_wiki = match_freq + restate_freq + paraphrase_freq + rewrite_freq + example_freq + express_freq + explain_freq + defend_freq + distinguish_freq + summarize_freq + interrelate_freq + interpret_freq + extend_freq


file.write("<p><b>Comprehension</b> repeated: "+str(comprehension_frequency_wiki)+" times</p>")

organize_freq = (all_words["organize"])
generalize_freq = (all_words["generalize"])
dramatize_freq = (all_words["dramatize"])
prepare_freq = (all_words["prepare"])
produce_freq = (all_words["produce"])
choose_freq = (all_words["choose"])
sketch_freq = (all_words["sketch"])
apply_freq = (all_words["apply"])
solve_freq = (all_words["solve"])
draw_freq = (all_words["draw"])
show_freq = (all_words["show"])
paint_freq = (all_words["paint"])


application_frequency_wiki = organize_freq + generalize_freq + dramatize_freq + prepare_freq + produce_freq + choose_freq + sketch_freq + apply_freq + solve_freq + draw_freq + show_freq + paint_freq

file.write("<p><b>Application</b> repeated: "+str(application_frequency_wiki)+" times</p>")

compare_freq=(all_words["compare"])
analyze_freq =(all_words["analyze"])
classify_freq = (all_words["classify"])
pointout_freq = (all_words["point"])
distinguish_freq = (all_words["distinguish"])
categorize_freq = (all_words["categorize"])
differentiate_freq = (all_words["differentiate"])
subdivide_freq = (all_words["subdivide"])
infer_freq = (all_words["infer"])
survey_freq = (all_words["survey"])
select_freq = (all_words["select"])
prioritize_freq = (all_words["prioritize"])


analysis_frequency_wiki = compare_freq + analyze_frequcny + classify_freq + pointout_freq + distinguish_freq + categorize_freq + differentiate_freq + subdivide_freq + infer_freq + survey_freq + select_freq + prioritize_freq


file.write("<p><b>Analysis</b> repeated: "+str(analysis_frequency_wiki)+" times</p>")

compose_freq =(all_words["compose"])
originate_freq = (all_words["originate"])
hypothesize_freq =(all_words["hypothesize"])
develop_freq = (all_words["develop"])
design_freq =(all_words["design"])
combine_freq = (all_words["combine"])
construct_freq = (all_words["construct"])
produce_freq = (all_words["produce"])
plan_freq = (all_words["plan"])
create_freq = (all_words["create"])
invent_freq =(all_words["invent"])
organize_freq = (all_words["organize"])


synthesis_frequency_wiki = compose_freq + originate_freq + hypothesize_freq + develop_freq + design_freq + combine_freq + construct_freq + produce_freq + plan_freq + create_freq + invent_freq + organize_freq


file.write("<p><b>Synthesis</b> repeated: "+str(synthesis_frequency_wiki)+" times</p>")

judge_freq=(all_words["judge"])
relate_freq = (all_words["relate"])
weight_freq = (all_words["weight"])
criticize_freq = (all_words["criticize"])
support_freq = (all_words["support"])
criticize_freq = (all_words["criticize"])
support_freq = (all_words["support"])
evaluate_freq = (all_words["evaluate"])
consider_freq = (all_words["consider"])
critique_freq = (all_words["critique"])
recommend_freq = (all_words["recommend"])
summarize_freq = (all_words["summarize"])
appraise_freq = (all_words["appraise"])
compare_freq = (all_words["compare"])


evaluation_frequency_wiki = judge_freq + relate_freq + weight_freq + criticize_freq + support_freq + evaluate_freq + consider_freq + critique_freq + recommend_freq + summarize_freq + appraise_freq + compare_freq


file.write("<p><b>Evaluation</b> repeated: "+str(evaluation_frequency_wiki)+" times</p>")
file.write("<hr><br><br><br>")

bottom = """


  </div>
</div>
</div>

</div>
<div class="card text-center">
  <div class="card-header">
    Thank you
  </div>
  <div class="card-body">
    <a href="/" class="btn btn-dark">Go to main</a>
  </div>
  </div>
</div>

</div>
</div>
</div>
</div>
</body>
</html>
"""
file.write(bottom)

file.close()
"""////////////////////////////////////////////////////////////////"""
