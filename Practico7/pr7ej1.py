import math
from random import random
from scipy.stats.distributions import chi2


def estimador_T_fijo():
	values  = [141, 291, 132]
	pi      = [0.25, 0.5, 0.25]
	resultado = 0
	n       = 564
	
	for i in range(3):
		resultado += ((values[i] - n*pi[i])**2)/float(n*pi[i])
	return resultado

def valor_p(T, k):
	return chi2.sf(T,k-1)

def generador_valores(n):
	suma = 0
	values = [0,0,0]
	
	for _ in range(n):
		value = random()
		if (value < 0.5):
			values[0] += 1
		elif (value < 0.75):
			values[1] += 1
		else:
			values[2] += 1
	for i in range(3):
		suma += values[i]
	return values

def estimador_T_variable(n):
	values = generador_valores(n)
	pi     = [0.5, 0.25, 0.25]
	resultado = 0
	n       = 564

	for i in range(3):
		resultado += ((values[i] - n*pi[i])**2)/float(n*pi[i])
	return resultado
	
def simulacion(t, n, r):
	contador = 0
	for _ in range(r):
		T = estimador_T_variable(n)
		if (T >= t):
			contador += 1
	return contador/float(r)

#print estimador_T_fijo()
#print(valor_p(estimador_T_fijo(), 3))
print(simulacion(estimador_T_fijo(), 564, 100))
