import math
from random import random

muestra = [122, 133, 106, 128, 135, 126]

def generator_lambda(values):
	result = 0
	n = len(values)

	for i in values:
		result += i  

	return  n / float(result)

lamda = generator_lambda(muestra)

def funcion(x, lamda):
	return 1 - math.e**(-x*lamda)

def generator_expo_values(n):
	values = []

	for _ in range(n):
		values.append(- math.log(random()) *100)

	return values

def generator_d(muestra, f, l):
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
		d_aux = max((i+1)/float(n) - f(x, l), f(x, l) - i/float(n))
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

d = generator_d(muestra, funcion, lamda)
print "lamda: ", lamda
print "estadistico: ", d
print "valor-p: ", valor_p(500, d, 10)
