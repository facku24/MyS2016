from random import random
from scipy.stats.distributions import chi2
import math

LLEGADAS = [18, 24, 16, 19, 25]
RANGOS   = [1010, 960, 1180, 985, 1118]

#------------------------------------------
#		VERIFICACION POISSON HOMOGENEO
#------------------------------------------
def generator_media(valores):
	M = 0
	n = len(valores)

	for i in valores:
		M += i

	return M / float(n)

def generator_varianza(valores, media):
	S2 = 0
	n = len(valores)

	for i in valores:
		S2 += (i - media)**2 / float(n - 1)

	return S2

def generator_T(media, varianza):
	return varianza / float(media)

def generator_poisson(lamda):
	U = random()
	i = 0
	p = math.e**(-lamda)
	F = p
	
	while U >= F:
		p = (lamda*p)/(i+1)
		F += p
		i += 1
	
	return i

def simulation(lamda, t):
	sup = 0
	inf = 0
	
	for _ in range(500):
		values = []
		
		for _ in range(5):
			values.append(generator_poisson(lamda))
		
		media = generator_media(values)
		varianza = generator_varianza(values, media)

		T = generator_T(media, varianza)

		if T >= t:
			sup += 1
		else:
			inf += 1

	p = 2 * min(sup/float(500), inf/float(500))

	return p

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

def valor_p(T, m):
	return 2* min(1 - chi2.sf(T,m-1), chi2.sf(T,m-1))

print sum(LLEGADAS)
media = generator_media(LLEGADAS)
print media
varianza = generator_varianza(LLEGADAS, media)
print varianza
T = generator_T(media, varianza)
print "T: ", T
#print "simulation p: ", simulation(media, T)
R = estadistico_R(RANGOS, LLEGADAS)
print R
print "valor-p: ", valor_p(R, 5)