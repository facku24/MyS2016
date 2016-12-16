import math
from random import random
from scipy.stats.distributions import chi2

def estimador_T_fijo():
	values  = [158, 172, 164, 181, 160, 165]
	pi      = 1/float(6)
	resultado = 0
	n 		= 1000
	n_pi    = 1000/float(6)
	
	for i in range(6):
		resultado += ((values[i] - n_pi)**2)
	return resultado/float(n_pi)

def valor_p(T, k):

	return chi2.sf(T,k-1)

def generador_valores(n):
	suma = 0
	values = [0,0,0,0,0,0]
	
	for _ in range(n):
		value = random()
		i = 0
		paso = 1/float(6)
		pi = paso
		while (value > pi):
			i+=1
			pi+= paso
		values[i] += 1	

	for i in range(6):
		suma += values[i]
	return values

def estimador_T_variable(n):
	values = generador_valores(n)
	pi     = 1/float(6)
	resultado = 0
	n_pi       = n/float(6)

	for i in range(6):
		resultado += ((values[i] - n_pi)**2)
	return resultado/float(n_pi)
	
def simulacion(t, n, r):
	contador = 0
	for _ in range(r):
		T = estimador_T_variable(n)
		if (T >= t):
			contador += 1
	return contador/float(r)

#print estimador_T_fijo()
#print(valor_p(estimador_T_fijo(), 6))
print(simulacion(estimador_T_fijo(), 500, 100))
