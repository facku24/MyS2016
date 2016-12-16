import math
from random import random

def funcion(x):
	return 1 - math.e**(-x)

def generator_expo_values(n):
	values = []

	for _ in range(n):
		values.append(- math.log(random()))

	return values

def generator_d(muestra, f):
	'''
	Esta funcion me generea el valor d necesario para calcular
	el p-valor despues
	l 	- lambda 
	'''
	muestra.sort()
	n = len(muestra)
	d = 0

	for i in range(n):
		x = muestra[i]
		d_aux = max((i+1)/float(n) - f(x), f(x) - i/float(n))
		d = max(d, d_aux)

	return d

def generator_D(tam):
	'''
	Esta funcion me va generando valores D, que despues se
	promedian y generan el valor-p
	'''
	values = []
	d = 0
	n = tam

	for _ in range(n):
		values.append(random())
	values.sort()

	for i in range(n):
		x = values[i]
		d_aux = max((i+1)/float(n) - x, x - i/float(n))
		d = max(d, d_aux)
	
	return d

def valor_p(repet, d, tam_muestra):
	tam = tam_muestra
	contador = 0
	for _ in range(repet):
		D = generator_D(tam)
		if (D >= d):
			contador += 1

	return contador / float(repet)

muestra1 = [0.08, 0.11, 0.20, 0.43, 0.52, 0.71, 2.25, 2.65, 2.801, 3.68]
muestra2 = [0.17, 0.27, 0.29, 0.38, 0.42, 0.5, 0.71, 1.98, 2.05, 2.27]
#muestra = generator_expo_values(10)
d = generator_d(muestra1, funcion)
print "muestra1: ", muestra1
print "estadistico1: ", d
print "valor-p1: ", valor_p(500, d, 10)

d = generator_d(muestra2, funcion)
print "muestra2: ", muestra2
print "estadistico2: ", d
print "valor-p2: ", valor_p(500, d, 10)
