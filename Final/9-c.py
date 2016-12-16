import math
from random import random

MUESTRA = [66, 72, 81, 94, 112, 116, 124, 140, 145, 155]

def funcion(x):
	return 1 - math.e**(-x/float(100))

def generator_expo_values(n):
	values = []

	for _ in range(n):
		values.append(- math.log(random()) *100)

	return values

def generator_d(muestra, f):
	'''
	Esta funcion me generea el valor d necesario para calcular
	el p-valor despues
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

muestra = generator_expo_values(10)
#print muestra
d = generator_d(muestra, funcion)
print d
#print generator_D(3)
print valor_p(500, d, 10)
#print generator_expo_values(10)