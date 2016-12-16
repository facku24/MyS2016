from random import random
import math
N = 10000

def real():
	resultado = 0
	for i in range(N):
		resultado += math.e**((i+1) / float(N))
	print resultado 

def ej4_6(n):
	resultado = 0
	for _ in range(n):
		U = int(random() * N) + 1
		resultado += math.e**(U / float(N))
	print resultado * N/n

real()
ej4_6(100)