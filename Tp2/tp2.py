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
	graph = G1
	index_init = int(10*random())
	next_index = index_init
	counters = []

	#inicializamos el arreglo contadores
	for _ in range(len(G1)):
		counters.append(0)

	print index_init
	for _ in range(1000):
		row = graph[next_index]
		new_step = next_step(len(row))
		next_index = row[new_step]
		counters[next_index] += 1

	for i in range(len(G1)):
		counters[i] = counters[i]/float(1000)
	print counters

def test():
	matrix = g2p(G1)
	print G1[1], matrix[1]

#for _ in range(5):
ej1()

