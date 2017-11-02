#!/usr/bin/env python3

import sys
import random
import pycorpora
import datetime
import re

# # #

NAME = 'Ten Second Summaries'
PREAMBLE = 'A catalogue of novels for NaNoGenMo 2017'
AUTHORED_BY = 'Andrew Zyabin'

# # #

def para(*objects, sep=' ', flush=False):
	print(*objects, sep=sep, end='\n\n', file=sys.stdout, flush=flush)

# # #

seed = sys.argv[1] if len(sys.argv) > 1 else str(random.random())

rn = random.Random(seed)

grammar = {
	'*': ['## {{story name}}\n\n{{story summary}}'],

	'noun': pycorpora.words.nouns['nouns'],
	'Noun': list(map(lambda a: a.capitalize(),
		pycorpora.words.nouns['nouns'])),
	'verb': list(map(lambda a: a['present'],
		pycorpora.words.verbs['verbs'])),
	'adj': pycorpora.words.adjs['adjs'],
	'Adj': list(map(lambda a: a.capitalize(),
		pycorpora.words.adjs['adjs'])),
	'occupation': pycorpora.humans.occupations['occupations'],

	'who': ['A {{occupation}}', 'A {{adj}} {{occupation}}'],
	'does what': ['{{verb}}s', '{{verb}}s a {{noun}}',
		'{{verb}}s a {{adj}} {{noun}}'],

	'story name': ['{{Noun}}', '{{Adj}} {{Noun}}'],
	'story summary': ['{{who}} {{does what}}.']
}

# # #

para('#', '_' + NAME + '_')
para(PREAMBLE)
para('Authored by', AUTHORED_BY)
para('Reproducible seed:', seed)
para('Last update:', datetime.date.today().isoformat())
para('* * *')

# # #

words = 0

while words < 50000:
	p = rn.choice(grammar['*'])
	while True:
		match = re.search('{{(.+?)}}', p)
		if match:
			p = p.replace(match[0], rn.choice(grammar[match[1]]))
		else:
			break
	para(p)
	words += len(p.split())

# # #

para('* * *')
para('And last but not least...')
para('## Ten Second Summaries')
para('A something-maker generates summaries at a computer with Python for fun',
	'by making a program for NaNoGenMo 2017.')
