from random import random
import math

def ej5_6():
	U = random()
	X = - math.log(1 - (1 - math.e**(-0.05))*U)
	return X

def rept(n):
	resultado = 0
	for _ in range(n):
		resultado += ej5_6()
	return resultado / float(n)

print rept(10000)