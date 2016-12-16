from random import random

def ej4_1():
	U = random()
	if (U > 1/float(3)):
		return 2
	return 1 

def ej4_3():
	U = random()
	if (U < 0.35):
		return 3
	if (U < 0.65):
		return 1
	if (U < 0.85):
		return 2
	return 4

def repet(n, function):
	result = 0
	for _ in range(n):
		value = function()
		if value == 1 :
			result += 1
	return result / float(n)

print repet(1, ej4_1)