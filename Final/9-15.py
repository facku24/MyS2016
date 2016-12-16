import numpy as np
import math
import scipy.stats as st
from scipy.stats.distributions import chi2
from random import random

muest1 = [121, 144, 158, 169, 194, 211, 242]
muest2 = [ 99, 128, 165, 193, 242, 265, 302]
muest3 = [129, 134, 137, 143, 152, 159, 170]

#-----------------------------------------------------
#				GENERADOR DE RANGO
#-----------------------------------------------------
def rango_i(totalset, subset):
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

r1 = rango_i(muest1+muest2+muest3, muest1)
r2 = rango_i(muest1+muest2+muest3, muest2)
r3 = rango_i(muest1+muest2+muest3, muest3)
#print r1, r2, r3

def estadistico_R(r_values, len_values):
	'''
	r_values 	- una lista con cada Ri calculado para cada muestra
	len_values 	- una lista con las longitudes de cada muestra
	'''
	R = 0
	n = sum(len_values)
	m = len(r_values)
	for i in range(m):
		ri = r_values[i]
		ni = len_values[i]
		R += ((ri - ni*(n+1)/float(2))**2) / float(ni)

	R = R * 12/ float(n*(n+1))

	return R

R = estadistico_R([r1, r2, r3], [7, 7, 7])
print "Estadistico R: ", R

def valor_p(T, m):
	return chi2.sf(T,m-1)

p = valor_p(R, 3)
print "p_value por ji: ", p

#-----------------------------------------------------
#			GENERADOR DE P-VALOR SIMULACION
#-----------------------------------------------------
def generador_subset(valores, n):
	'''
	Esta funcion me genera un subconjunto de n valores, desde el conjunto Valores.

	valores - los valores de los cuales armo mi subconjunto
	n 		- la longitud de mi subconjunto
	'''
	length = len(valores)
	listado = valores

	contador = n
	k = length-1

	while (contador > 0):
		u = int(length * random())
		aux = listado[k]
		listado[k] = listado[u]
		listado[u] = aux
		k -= 1
		contador -= 1

	return listado[len(valores)-n: ]

def simulacion(valores, t, n):
	'''
	t 	- estadistico
	n 	- cantidad de veces que realizamos la simulacion
	'''
	contador = 0

	for _ in range(n):
		r_values = []
		len_values = []
		R = 0

		for i in range(3):
			subconjunto = generador_subset(valores, 7)
			r_values.append(rango_i(valores, subconjunto))
			len_values.append(7)

		R = estadistico_R(r_values, len_values)

		p = valor_p(R, 3)

		if p >= t:
			contador += 1
			
	return contador / float(n)

print "p_value por simulacion: ", simulacion(muest1+muest2+muest3, p, 1000)