from random import random

def ej4_3():
	U = random()
	if (U < 0.35):
		return 3
	if (U < 0.65):
		return 1
	if (U < 0.85):
		return 2
	return 4

def repet(n):
	resultado = [0,0,0,0]
	for _ in range(n):
		value = ej4_3()
		resultado[value-1] +=1
	print resultado

repet(10000)