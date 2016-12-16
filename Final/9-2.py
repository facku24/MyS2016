from random import random
from scipy.stats.distributions import chi2
import math

#---------------------------------------------
#			CONSTANTES
#---------------------------------------------
N = 6
REPET = 1000
npi = 500/float(3)
values = [158, 172, 164, 181, 160, 165]
probs = [1/float(6), 1/float(6), 1/float(6), 1/float(6), 1/float(6), 1/float(6)]

#---------------------------------------------
#			COMPUTO
#---------------------------------------------
def generator_T(values, probs):
	'''
	Esta funcion genera mi estadistico T en base
	a la muestra y a las probabilidades que tiene
	cada valor en el rango
	'''
	resultado = 0
	n       = sum(values)
	for i in range(len(values)):
		resultado += ((values[i] - npi)**2)
	return resultado / npi

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

def generator_values(repet, n, probs):
	'''
	repet 	- La cantidad de veces valores a generar
	n 		- La cantidad de valores diferentes que toma la variable
	probs 	- Las probabilidades de los diferentes valores
	'''

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
		values = generator_values(REPET, N, probs)
		T = generator_T(values, probs)

		if T >= t:
			counter += 1
	return counter / float(repet)

simulation = generator_simulation(500, probs, T)
print "valor_p(T) simulated: ", simulation