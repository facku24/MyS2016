from te2_pagerank import *
from random import random

def next_step(n):
	counter = 0
	step = 1/float(n)
	limit = step
	ran = random()
	while (ran > limit):
		counter += 1
		limit += step
	return counter

def ej1():
	matrix = g2p(G1)
	index_init = int(10*random())

def test():
	matrix = g2p(G1)
	print G1[1], matrix[1]

next_step(4)
