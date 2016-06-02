import math
from random import random
from scipy.stats.distributions import chi2


def estimador_T_fijo():
	values  = [158,172,164,181,160,165]
	pi      = 1/float(6)
	resultado = 0
	npi       = 1000*pi
	
	for i in range(6):
		resultado += ((values[i] - npi)**2)/float(npi)
	return resultado

def valor_p(T, k):
	return chi2.sf(T,k-1)

def generador_valores(n):
	suma = 0
	values = [0,0,0,0,0,0]
	pi = 1/float(6)
	for _ in range(n):
		value = random()
		if (value < pi):
			values[0] += 1
		elif (value < 2*pi):
			values[1] += 1
		elif (value < 3*pi):
			values[2] += 1
		elif (value < 4*pi):
			values[3] += 1
		elif (value < 5*pi):
			values[4] += 1
		else:
			values[5] += 1
	return values

def estimador_T_variable(n):
	values = generador_valores(n)
	pi     = 1/float(6)
	n       = 1000
	npi = n*pi
	resultado = 0

	for i in range(6):
		resultado += ((values[i] - npi)**2)/float(npi)
	return resultado
	
def simulacion(t, n, r):
	contador = 0
	for _ in range(r):
		T = estimador_T_variable(n)
		if (T >= t):
			contador += 1
	return contador/float(r)

print(valor_p(estimador_T_fijo(), 6))
print(simulacion(estimador_T_fijo(), 1000, 100))
