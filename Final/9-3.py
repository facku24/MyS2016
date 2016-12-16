import numpy as np
import math
import scipy.stats as st
from random import random

#-----------------------------------------------------
#			CONSTANTES
#-----------------------------------------------------
muestra = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
A = 0
B = 1
N = 10
#-----------------------------------------------------
#			GENERADOR DE MUESTRA UNIFORMES
#-----------------------------------------------------
def uniform_distro(x):
	return (x - A) / float(B - A)

def uniform_generator(n):
	values = []

	for _ in range(n):
		v = int(random() * 40) + 1
		values.append(v)

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
	tam 	- cantidad de elementos en la muestra
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

d = generator_d(muestra, uniform_distro)
print d
#print generator_D(3)
print valor_p(500, d, 10)
#print generator_expo_values(10)

#-----------------------------------------------------
#			SIMULACION
#-----------------------------------------------------
def generator_unif_values(n):
	values = []

	for _ in range(n):
		values.append(random())

	return values

def generator_simulation(repet, f, d):
	counter = 0

	for _ in range(repet):
		values = generator_unif_values(N)
		D = generator_d(values, f)

		if D >= d:
			counter += 1
	return counter / float(repet)

simulation = generator_simulation(500, uniform_distro, d)
print "valor_p(T) simulated: ", simulation