from random import random
import math

def gen_poisson(param):
	U = random()
	i = 0
	p = math.e**(-param)
	F = p
	while (U >= F):
		p = (param * p)/float(i+1)
		F += p
		i += 1
	
	return i

def metodo_acept_rech(k):
	poisson =  gen_poisson()
	while
	if (poisson <= K)
