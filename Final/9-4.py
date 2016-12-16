import numpy as np
import math
import scipy.stats as st
from random import random

#-----------------------------------------------------
#			CONSTANTES
#-----------------------------------------------------
muestra = [164, 142, 110, 153, 103, 52, 174, 88, 178, 184, 58, 62, 132, 128]
A = 50
B = 200
N = 10
#-----------------------------------------------------
#			GENERADOR DE MUESTRA UNIFORMES
#-----------------------------------------------------
def uniform_distro(x):
	return (x - A) / float(B - A)

def generator_unif_values(n):
	'''
	Genera valores uniformes en el intervalo (50, 200)
	'''
	values = []

	for _ in range(n):
		v = int(random() * 151) + 51
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
print valor_p(500, d, 10)

#-----------------------------------------------------
#			SIMULACION
#-----------------------------------------------------
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