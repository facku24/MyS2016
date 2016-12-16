from random import random
from scipy.stats.distributions import chi2
import math

N = 8
CANT = 16
MUESTRA = [6, 7, 3, 4, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]

print sum(MUESTRA) / float(16)

def generator_vector(values, n):
	'''
	Esta funcion, dado un vector de observaciones, genera el vector 
	correspondiente de valores acumuladors de las observaciones para 
	cada uno de los mismos.
	'''

	vector = []
	cant = len(values)

	for _ in range(n+1):
		vector.append(0)

	for i in range(cant):
		vector[values[i]] += 1

	return vector

vector = generator_vector(MUESTRA, N)

def generator_media(values):
	media = 0
	n = len(values)

	for i in range(n):
		media += values[i]

	return media / float(n)

print generator_media(MUESTRA)
p =  generator_media(MUESTRA) / float(N)
print "p: ", p

def binomial(n,k):
	'''
	Simplement calcula el binomio de newton
	para los valores n, k
	'''
	fact = math.factorial
	return fact(n)/float(fact(k)*fact(n-k))

def generator_probs(n, p):
	'''
	Esta funcion me genera el vector de probabilidades
	para mi v.a. binomial(n,p)
	'''
	probs = []
	for i in range(N+1):
		prob_i = binomial(N, i) * (p**i) * ((1-p)**(N-i))
		probs.append(prob_i)
	return probs

probs =  generator_probs(N, p)
#print probs

def generator_T(values, probs):
	'''
	Esta funcion genera mi estadistico T en base
	a la muestra y a las probabilidades que tiene
	cada valor en el rango
	'''
	resultado = 0
	n       = sum(values)
	cant = len(values)

	for i in range(cant):
		npi = n*probs[i]
		resultado += ((values[i] - npi)**2)/float(npi)
	return resultado

def valor_p(T):
	return chi2.sf(T,N-1)



#-----------------------------------------
#			SIMULACION
#-----------------------------------------
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

def generator_v_binomiales(cant, n, probs):
	'''
	cant 	- La cantidad de variables a generar
	n 		- Limite superior de valores que toma nuestra variable	
	probs 	- Las probabilidades para cada valor
	'''
	values = []

	for _ in range(cant):
		U = generator_v_a_bin(n, probs)
		values.append(U)

	return values

def generator_T_prom(times, value, probs, p):
	'''
	En el caso de que mi primer T valor estimado este cerca de un valor 
	critico, simulamos 
	'''
	promedio = 0
	for _ in range(times):
		values = generator_v_binomiales(16, 8, p)
		vector = generator_vector(values, 8)
		T = generator_T(vector, probs)

		if T > value:
			promedio += 1
	
	promedio = promedio / float(times)
	
	return promedio

T = generator_T(vector, probs)
print "Estadistico T: ", T
print "valor-p: ", valor_p(T)
print "valor-p (sim): ", generator_T_prom(100, 18.7, probs, p)