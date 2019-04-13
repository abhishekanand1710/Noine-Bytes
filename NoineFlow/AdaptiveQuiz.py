# first question
import pandas as pd
from Correlator import cluster
from Recommender import recommend
import json

ability_level = 0.0
chance = 3
cur_id = 0
next_id = 0
l_attempts = 0

ranks = {
	1: {
		'c': 0.3,
		'w': -0.1,
		'uth': 0.6,
		'lth': 0.0,
		'bf': 0.9
		},
	2: {
		'c': 0.5,
		'w': -0.2,
		'uth': 1.3,
		'lth': 0.7,
		'bf': 1.3
		},
	3: {
		'c': 0.8,
		'w': -0.3,
		'uth': 3.1,
		'lth': 1.9,
		'bf': 0.0
		}
	}

history = {}

response = True

def ability(id, response, ability_level, hlen, history):
	if(response):
		if(ability_level>1.3):
			old_level =3
			ability_level = ability_level + ranks[3]['c']
			#history[cur_id] = 1
			#print unrelated ques.. handle it down
		elif(ability_level>0.7):
			old_level = 2
			ability_level = ability_level + ranks[2]['c']
			#history[cur_id] = 1
		else:
			ability_level = ability_level + ranks[1]['c']
			old_level = 1
			#history[cur_id] = 1
	else:
		if hlen == 3:
			mult = 0.3
		elif hlen == 2:
			mult = 0.2
		else:
			mult = 0.1

		if(ability_level>1.9):
			old_level = 3
			ability_level = ability_level + mult*ranks[3]['w']
			#history[cur_id] = 0
			#print unrelated ques.. handle it down
		elif(ability_level>0.7):
			old_level = 2
			ability_level = ability_level + mult*ranks[2]['w']
			#history[cur_id] = 0
		else:
			old_level = 1
			ability_level = ability_level + mult*ranks[1]['w']
			#history[cur_id] = 0

	if(ability_level>1.3):
		difficulty_level = 3
	elif(ability_level>0.7):
		difficulty_level = 2
	else:
		difficulty_level = 1

	switch = False
	resource = False
	one = False
	zero = False
	if old_level != difficulty_level:
		switch = True
	elif hlen == 3:
		for key, val in history.items():
			if val == 0:
				zero = True
			if val == 1:
				one = True
		if(zero and one):
			resource = True

	return ability_level, difficulty_level, id, switch, resource

def get_ques(id):
	df = pd.read_csv('../NoineEngine/Questions_Rank.csv', index_col = False)
	ques = df.loc[df['ID'] == id].to_dict()
	q_dict = {}
	for q, val in ques.items():
		for k,qval in val.items():
			q_dict[q] = qval

	return json.dumps(q_dict)

def quizhandler(id , response, hist = {}, ability_level = 0.0):
	ability_level, difficulty_level, cur_id, switch, resource = 0, 0, 0, False, False
	hist[id] = response

	print(hist)
	print(id)
	ability_level, difficulty_level, cur_id, switch, resource = ability(id, response, ability_level, len(hist), hist)

	corr = False
	if (not response): corr = True

	if len(hist) == 3:
		if switch:
			print(cur_id, corr, difficulty_level)
			next_id = cluster(cur_id, corr, 3)
			ques = get_ques(next_id)
			print(next_id)
			# bhargave needs question, ability_level, send history=0
			return(
				ability_level,
				next_id,
				ques,
				0,
				0
			)
		elif resource:
			# cur_id
			print(cur_id, corr, difficulty_level)
			next_id = cluster(cur_id, corr, 3)
			ques = get_ques(next_id)
			print(next_id)
			resource_link = recommend(cur_id)
			#bhargav additional apart from above  is resource
			return(
				ability_level,
				next_id,
				ques,
				resource_link,
				0
			)
	elif len(hist) == 2:
		print(cur_id, corr, difficulty_level)
		next_id = cluster(cur_id, corr, 3)
		ques = get_ques(next_id)
		print(ques)
		# bhargave needs question, ability_level, send history=2
		return(
				ability_level,
				next_id,
				ques,
				0,
				2
			)
	else:
		print(cur_id, corr, difficulty_level)
		next_id = cluster(cur_id, corr, 3)
		ques = get_ques(next_id)
		print(ques)
		# bhargave needs question, ability_level, send history=1
		return(
				ability_level,
				next_id,
				ques,
				0,
				1
			)