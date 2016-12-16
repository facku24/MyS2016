from random import random
import numpy as np
import math
import scipy.stats as st

tratamiento = [19, 31, 39, 45, 47, 66, 75]
control = [28, 36, 44, 49, 52, 72, 73]

def generador_subset(total_set, longitud):
	'''
	Esta funcion genera un subconjunto del conjunto total.

	param - total_set: El conjunto total. No requiere que este ordenado
	'''

	length = len(total_set)
	k = length-1

	while (k > 0):
		u = int(length * random())
		aux = total_set[k]
		total_set[k] = total_set[u]
		total_set[u] = aux
		k -= 1

	return total_set[0: longitud]

def rango(totalset, subset):
	'''
	This function generates the rank fot subset.

	param - totalset: Debe de ser el conjunto total y ordenado de todas las muestras
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
				break
			else:
				index+=1
	return rango

def p_valor_gen(n, m, t):
	'''
	Esta funcion calcula el valor exacto del p-valor mediante recursion.

	param - n: la cantidad de datos de la muestra mas chica
	param - m: la cantidad de datos de la muestra mas grande
	param - t: el rango obtenido de la muestra chica
	'''

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

def p_valor_normal_gen(n, m, r):
	'''
	Esta funcion calcula el valor del p-valor mediante la aproximacion
	con la distribucion normal.

	param - n: la cantidad de datos de la muestra mas chica
	param - m: la cantidad de datos de la muestra mas grande
	param - t: el rango obtenido de la muestra chica
	'''

	numerador = r - n * (n+m+1)/float(2)

	value = numerador / float(math.sqrt(n*m*(n+m+1)/float(12)))
	normal = st.norm()
	if (numerador > 0):
		return 2* (1-normal.cdf(value))
	else:
		return 2* (normal.cdf(value))

def p_valor_simulacion_gen(n, totalset, t):
	p_inf = 0
	p_sup = 0

	for _ in range(n):
		subset = generador_subset(totalset, 7)
		r = rango(totalset, subset)
		print"rango sim: ", r
		if (r <= t):
			p_inf += 1
		if (r >= t):
			p_sup += 1
	value = min(p_inf/float(n), p_sup/float(n))

	return 2*value


muestra_total = tratamiento + control
muestra_total.sort()

ranke = rango(muestra_total, tratamiento)
p_valor = p_valor_gen(len(tratamiento), len(control), ranke)
p_valor_normal = p_valor_normal_gen(len(tratamiento), len(control), ranke)
p_valor_simulacion = p_valor_simulacion_gen(10, muestra_total, ranke)

print "rango original: ", ranke
print "p-valor: ", p_valor
print "p-valor normal: ", p_valor_normal
print "p-valor simulado:", p_valor_simulacion