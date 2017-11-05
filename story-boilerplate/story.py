#!/usr/bin/env python3

import sys
import random
import datetime
import re

# # #

NAME = ''
PREAMBLE = 'A novel for NaNoGenMo 2017'
AUTHORED_BY = 'Andrew Zyabin'

# # #

GRAMMAR = {
	'*': []
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
		match = re.search('{{(.+?)}}', p)
		if match:
			p = p.replace(match[0], rn.choice(GRAMMAR[match[1]]))
		else:
			break
	para(p)
	words += len(p.split())
