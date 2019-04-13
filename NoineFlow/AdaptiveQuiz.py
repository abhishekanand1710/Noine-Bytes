# first question
import pandas as pd

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

def ability(id, resource, ability_level):
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
		if(len(history) == 3:
			mult = 0.3
		elif(len(history) == 2:
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
	elif len(history) == 3:
		for key, val in history:
			if val == 0:
				zero = True
			if val == 1:
				one = True
		if(zero and one):
			resource = True

	return ability_level, difficulty_level, id, switch, resource

def get_ques(id):
	df = pd.read_csv('Questions_Rank.csv')
	ques = df.loc[df['ID'] == id].to_json()
	return ques

def main(id , response, hist = {}, ability_level):
	ability_level, difficulty_level, cur_id, switch, resource = 0, 0, 0, False, False
	hist[id] = response
	for hkey, hval in hist:
		ability_level, difficulty_level, cur_id, switch, resource = ability(hkey, hval, ability_level)

	corr = False
	if !response: corr = True

	if len(hist) == 3:
		if switch:
			next_id = cluster(cur_id, corr, difficulty_level)
			ques = get_ques(next_id)
			# bhargave needs question, ability_level, send history=0
		elif resource:
			# cur_id
			next_id = cluster(cur_id, corr, difficulty_level)
			ques = get_ques(next_id)
			#bhargav additional apart from above  is resource
	elif len(hist) == 2:
		next_id = cluster(cur_id, corr, difficulty_level)
		ques = get_ques(next_id)
		# bhargave needs question, ability_level, send history=2
	else:
		next_id = cluster(cur_id, corr, difficulty_level)
		ques = get_ques(next_id)
		# bhargave needs question, ability_level, send history=1