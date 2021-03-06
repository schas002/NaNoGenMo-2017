#!/usr/bin/env python3

import sys
import random
import pycorpora
import datetime
import re

# # #

NAME = 'Twenty Second Summaries'
PREAMBLE = 'A catalogue of novels for NaNoGenMo 2017'
AUTHORED_BY = 'Andrew Zyabin'

# # #

GRAMMAR = {
	'*': ['## {{story name}}\n\n{{story summary}}'],

	'#': list(map(lambda a: str(a), range(10))),

	'noun': pycorpora.words.nouns['nouns'],
	'Noun': list(map(lambda a: a.capitalize(),
		pycorpora.words.nouns['nouns'])),
	'verb': list(map(lambda a: a['present'],
		pycorpora.words.verbs['verbs'])),
	'adj': pycorpora.words.adjs['adjs'],
	'Adj': list(map(lambda a: a.capitalize(),
		pycorpora.words.adjs['adjs'])),
	'occupation': pycorpora.humans.occupations['occupations'],
	'room': pycorpora.architecture.rooms['rooms'],
	'passage': pycorpora.architecture.passages['passages'],

	'their': ['a', 'his', 'her', 'their'],
	'month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
		'August', 'September', 'October', 'November', 'December'],
	'yy': ['{{#}}{{#}}'],
	'year': ['20{{yy}}', '19{{yy}}', "'{{yy}}"],
	'week': ['week', 'day', 'month', 'year', 'decade'],

	'who': ['A {{occupation}}', 'A {{adj}} {{occupation}}'],
	'does what': ['{{verb}}s', '{{verb}}s a {{noun}}',
		'{{verb}}s a {{adj}} {{noun}}'],
	'where': ['at a {{room}}', 'at a {{passage}}', 'at a {{adj}} {{room}}',
		'at a {{adj}} {{passage}}'],
	'with what': ['with a {{noun}}', 'with a {{adj}} {{noun}}',
		'using a {{noun}}', 'using a {{adj}} {{noun}}'],
	'for what': ['for a {{noun}}', 'for a {{adj}} {{noun}}',
		'to {{verb}} {{their}} {{noun}}',
		'to {{verb}} {{their}} {{adj}} {{noun}}'],
	'how': ['by {{verb}}ing a {{noun}}', 'by {{verb}}ing an {{adj}} {{noun}}'],
	'when': ['in {{month}}', 'in {{year}}', 'in {{month}} {{year}}',
		'some time ago', 'a {{week}} ago'],

	'story name': ['{{Noun}}', '{{Adj}} {{Noun}}'],
	'story summary': ['{{who}} {{does what}} {{where}} {{with what}} ' +
		'{{for what}} {{how}} {{when}}.']
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

# # #

para('* * *')
para('And last but not least...')
para('## Twenty Second Summaries')
para('A something-maker generates summaries at a computer with Python for fun',
	'by making a program for NaNoGenMo 2017.')
