from random import random
from scipy.stats.distributions import chi2
import math

N = 50
P = 0.7
CANT = 10

def generator_v_a_bin(n, p):
	'''
	Esta funcion simplemente me genera un valor
	de la variable aleatoria binomial(n,p)
	'''
	U = random()
	c = p / float(1-p)
	i = 0
	pr = (1-p)**n
	F = pr
	while (U > F):
		pr = ((c*(n-i))/float(i+1))*pr
		F = F + pr
		i += 1
	X = i
	return X

def generator_vector(cant):
	'''
	Esta funcion genera un vector de valores de 
	observaciones para cada valor en el rango de
	la binomial. Se simula cant veces y cada resultado
	se guarda en su celda correspondiente
	'''
	vector = [0,0,0,0,0,0]

	for _ in range(cant):
		value = generator_v_a_bin(N, P)
		vector[value] += 1
	return vector

def generator_media(values):
	media = 0
	n = len(values)

	for i in range(n):
		media += values[i]

	return media/ float(n)

def generator_variance(values, media):
	n = len(values)
	varizance = 0

	for i in range(n):
		varizance += (values[i] - media)**2
	
	varizance = varizance/ float(n - 1)

	return varizance

def generator_v_binomiales(cant):
	values = []

	for _ in range(cant):
		U = generator_v_a_bin(N, P)
		values.append(U)

	return values

values = generator_v_binomiales(CANT)
print "values", values
media =  generator_media(values)
print "media: ", media
variance = generator_variance(values, media)
print "variance: ", variance

def generator_probs():
	'''
	Esta funcion me genera el vector de probabilidades
	para mi v.a. binomial(n,p)
	'''
	probs = []
	for i in range(N+1):
		prob_i = binomial(N, i) * (P**i) * ((1-P)**(N-i))
		probs.append(prob_i)
	return probs

def binomial(n,k):
	'''
	Simplement calcula el binomio de newton
	para los valores n, k
	'''
	fact = math.factorial
	return fact(n)/float(fact(k)*fact(n-k))

def generator_T(values, probs):
	'''
	Esta funcion genera mi estadistico T en base
	a la muestra y a las probabilidades que tiene
	cada valor en el rango
	'''
	resultado = 0
	n       = sum(values)
	for i in range(len(values)):
		resultado += ((values[i] - n*probs[i])**2)/float(n*probs[i])
	return resultado

def valor_p(T):
	return chi2.sf(T,N-1)

#new_values = generator_vector(CANT)
#probs = generator_probs()
#T = generator_T(new_values, probs)
#print new_values
#print T
#print valor_p(T)

def generator_T_prom(times, value):
	'''
	En el caso de que mi primer T valor estimado este cerca de un valor 
	critico, simulamos 
	'''
	promedio = 0
	for _ in range(times):
		vector = generator_vector(CANT)
		T = generator_T(vector, probs)
		if T > value:
			promedio += 1
	promedio = promedio / float(times)
	
	return promedio

#print generator_T_prom(40, 10.8057930007)