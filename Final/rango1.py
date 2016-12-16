import numpy as np
import math
import scipy.stats as st
from random import random

muB = [342, 361, 448, 453, 504]
siB = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]
muC = [0.076, 0.021, 0.096, 0.007, 0.149]
siC = [0.169, 0.165, 0.078, 0.062, 0.012, 0.007, 0.039, 0.030, 0.175, 0.23]
muA = [31, 33, 32, 37, 36]
siA = [37, 12, 20, 13, 29, 25, 33, 22, 26, 20]
mu2 = [6.53, 12.50, 4.34, 7.69, 12.41, 14.79, 11.02, 15.52, 43.40, 13.14]
mu1 = [6.98, 9.66, 3.53, 8.92, 12.9, 18.18, 15.56, 13.46, 42.25, 12.33]
muestra1 = [2,3,4]
muestra2 = [3,5,7]
muB = [132, 104, 162, 171, 129]
siB = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]


#-----------------------------------------------------
#			GENERADOR DE MUESTRA EXPONENCIAL
#-----------------------------------------------------
def exponencial_generator(n):
	valores = []

	for _ in range(n):
		U = -math.log(random()) / float(10)
		valores.append(U)

	return valores

#print exponencial_generator(5)

#-----------------------------------------------------
#			GENERADOR DE MUESTRA UNIFORMES
#-----------------------------------------------------
def uniform_generator(n):
	values = []

	for _ in range(n):
		v = int(random() * 40) + 1
		values.append(v)

	return values

#print uniform_generator(5)

#-----------------------------------------------------
#				GENERADOR DE RANGO
#-----------------------------------------------------
def rango(totalset, subset):
	'''
	Esta funcion me genera el rango para un subconjunto.

	param - totalset: Debe de ser el conjunto total de todas las muestras
					  simuladas y las muestras observadas
	param - subset: Debe de ser el subconjunto al cual le quiero generar el rango
	'''
	rango = 0
	index = 0

	totalset.sort()
	subset.sort()
	
	for elem in subset:
		while True:
			if (totalset[index] == elem):
				if (index < len(totalset)-1 and totalset[index] == totalset[index+1]):
					rango += (2*index+3) /float(2)
				elif (index > 0 and totalset[index] == totalset[index-1]):
					rango += (2*index+1) /float(2)
				else:
					rango += index + 1
					index += 1
				break
			else:
				index+=1
	return rango

r = rango(siA+muA, muA)
print r

#-----------------------------------------------------
#				GENERADOR DE P-VALOR RECURSIVO
#-----------------------------------------------------
def algoritmo_recursivo(n, m, t):
	p = {}

	for i in range(0, n+1):
		for j in range(0, m+1):
			for k in range(0, t+1):
				p[i, j, k] = 0

	#inicializaciones
	for i in range(1, n+1):
		for k in range(i * (i + 1)/2, t+1):
			p[i, 0, k] = 1

	for k in range(1, t+2):
		for j in range(1, m+1):
			p[0, j, k-1] = 1

	for i in range(1, n+1):
		for j in range(1, m+1):
			for k in range(1, t+1):
				if (k < i+j):
					p[i, j, k] = (j/float(i+j)) * p[i, j-1, k]
				else:
					value1 = (i / float(i+j))
					value2 = (j / float(i+j))
					p[i, j, k] =  value1 * p[i-1, j, k-i-j] +  value2 * p[i, j-1, k]

	if (p[n, m, t] < 1-p[n, m, t-1]):
		return 2*p[n, m, t]
	else:
		return 2*(1-p[n, m, t-1])

#p_value_recur = algoritmo_recursivo(5, 10, r)
#print "p_value por recursion: ", p_value_recur

#-----------------------------------------------------
#				GENERADOR DE P-VALOR NORMAL
#-----------------------------------------------------
def estimador_normal(n, m, r):
	'''

	n - tamanio de la primer muestra
	m - tamanio de la segunda muestra
	r - rango de la muestra total
	'''
	numerador =  n * (n+m+1)/float(2)

	value = (r - numerador) / float(math.sqrt(n*m*(n+m+1)/float(12)))
	normal = st.norm()

	if (numerador > r):
		return 2 * (normal.cdf(value))
	return 2* (1-normal.cdf(value))

p_value_norm = estimador_normal(5, 10, r)
print "p_value por normal: ", p_value_norm

#-----------------------------------------------------
#			GENERADOR DE P-VALOR SIMULACION
#-----------------------------------------------------
def generador_subset(muestras, simulaciones):
	length = len(muestras) + len(simulaciones)
	listado = muestras + simulaciones

	k = length-1

	while (k > 0):
		u = int(length * random())
		aux = listado[k]
		listado[k] = listado[u]
		listado[u] = aux
		k -= 1

	return listado[0: len(muestras)]

def rango(muestra, simulaciones, subset):
	rango = 0
	index = 0

	muestra_total = muestra + simulaciones
	muestra_total.sort()

	subset.sort()
	
	for elem in subset:
		while True:
			if (muestra_total[index] == elem):
				rango += index + 1
				break
			else:
				index+=1
	return rango

def simulacion(repet, t, muestras, simulaciones):
	p_inf = 0
	p_sup = 0

	for _ in range(repet):
		subset = generador_subset(muestras, simulaciones)
		r = rango(muestras, simulaciones, subset)
		if (r <= t):
			p_inf += 1
		if (r >= t):
			p_sup += 1
	value = min(p_inf/float(repet), p_sup/float(repet))

	return 2*value

print(simulacion(1000, r, muA, siA))
