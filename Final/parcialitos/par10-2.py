import math
from random import random

#-------------------------------------------------
#					CONSTANTES
#-------------------------------------------------
muestra = [0.65401, 0.019464, 0.0094966, 0.69783, 0.058019,0.02111,0.37748,0.014272, 
		  1.2275, 0.50268]
lamda = 2


def funcion(x):
	return 1 - math.e**(-x*lamda)

def generator_expo_values(n):
	values = []

	for _ in range(n):
		values.append(- math.log(random()) / float(lamda))

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

d = generator_d(muestra, funcion)
print "Estadistico d: ", d
N = len(muestra)
print "valor-p: ", valor_p(500, d, N)
print generator_expo_values(N)
#-----------------------------------------------------
#			SIMULACION
#-----------------------------------------------------
def generator_simulation(repet, f, d):
	counter = 0

	for _ in range(repet):
		values = generator_expo_values(N)
		D = generator_d(values, f)

		if D >= d:
			counter += 1
	return counter / float(repet)

simulation = generator_simulation(500, funcion, d)
print "valor_p(T) simulated: ", simulation