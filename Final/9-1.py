from random import random
from scipy.stats.distributions import chi2
import math

N = 3
values = [141, 291, 132]
probs = [0.25, 0.5, 0.25]

def generator_T(values, probs):
	'''
	Esta funcion genera mi estadistico T en base
	a la muestra y a las probabilidades que tiene
	cada valor en el rango
	'''
	resultado = 0
	n       = sum(values)
	for i in range(len(values)):
		resultado += ((values[i] - n*probs[i])**2)/float(n*probs[i])
	return resultado

def valor_p(T):
	return chi2.sf(T,N-1)

T = generator_T(values, probs)
print "T: ", T
print "valor_p(T): ", valor_p(T)

#---------------------------------------------
#			SIMULACION
#---------------------------------------------
def generator_value(probs):
	U = random()
	i = 0
	acum = probs[0]

	while(U > acum):
		i +=1
		acum += probs[i]

	return i

#print generator_value(probs)

def generator_values(repet, n, probs):
	values = []

	for _ in range(n):
		values.append(0)

	for _ in range(repet):
		value = generator_value(probs)
		values[value] += 1

	return values

def generator_simulation(repet, probs, t):
	counter = 0

	for _ in range(repet):
		values = generator_values(564, 3, probs)
		T = generator_T(values, probs)

		if T >= t:
			counter += 1
	return counter / float(repet)

simulation = generator_simulation(100, probs, T)

print "valor_p(T) simulated: ", simulation