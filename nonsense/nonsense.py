#!/usr/bin/env python3

import sys
import random
import pycorpora
import datetime
import re

# # #

NAME = 'Nonsense'
PREAMBLE = 'A realm of spewed-out nonsense for NaNoGenMo 2017'
AUTHORED_BY = 'Andrew Zyabin'

# # #

GRAMMAR = {
	'*': ['{{nonsense}}', '## {{nonsense}}', '- {{nonsense}}',
		'0. {{nonsense}}', '* * *'],

	'noun': pycorpora.words.nouns['nouns'],
	'Noun': list(map(lambda a: a.capitalize(),
		pycorpora.words.nouns['nouns'])),
	'verb': list(map(lambda a: a['present'],
		pycorpora.words.verbs['verbs'])),
	'Verb': list(map(lambda a: a['present'].capitalize(),
		pycorpora.words.verbs['verbs'])),

	'a': ['a', 'the', '{{.}}'],
	'A': ['A', 'The', '{{.}}'],
	'I': ['I', 'we', 'you', 'he', 'she', 'it', 'they'],

	'nonsense': ['{{noun nonsense}}{{.}}', '{{verb nonsense}}{{.}}'],
	'noun nonsense': ['{{noun}}{{.}}', '{{Noun}}{{.}}', '{{a}} {{noun}}{{.}}',
		'{{A}} {{noun}}{{.}}'],
	'verb nonsense': ['{{verb}}{{.}}', '{{Verb}}{{.}}', '{{I}} {{verb}}{{.}}',
		'how {{I}} {{verb}}?', '{{verb}} {{noun nonsense}}{{.}}',
		'{{Verb}} {{noun nonsense}}{{.}}'],
	'.': ['', '.', '..', '...', '!', '?']
}

# # #

def para(*objects, sep=' ', flush=False):
	print(*objects, sep=sep, end='\n\n', file=sys.stdout, flush=flush)

# # #

seed = sys.argv[1] if len(sys.argv) > 1 else str(random.random())

rn = random.Random(seed)

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
	p = rn.choice(GRAMMAR['*'])
	while True:
		match = re.search(r'{{(.+?)}}', p)
		if match:
			p = p.replace(match[0], rn.choice(GRAMMAR[match[1]]))
		else:
			break
	p = re.sub(r'a ([aeiou])', r'an \1', p)
	para(p)
	words += len(p.split())
