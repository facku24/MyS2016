from random import random
import numpy as np
import math
import scipy.stats as st
from scipy.stats.distributions import chi2

valores = [18, 24, 16, 19, 25]
rangos = [1010, 960, 1180, 985, 1118]

def media_gen(values):
	media = 0
	
	for i in values:
		media += i

	return media/float(len(values))

def variance_gen(values, media):
	variance = 0
	
	for i in values:
		variance += (i - media)**2

	return variance/float(len(values)-1)

def estimator_gen(values, media):
	variance = variance_gen(values, media)

	return variance/media

def poisson_va_gen(media):
	i = 0
	p = (1/float(math.e**media))
	f = p
	u = random()

	while(u > f):
		p = media*p/(i+1)
		f += p
		i += 1

	return i

def set_poisson_va_gen(n, media):
	variables = []

	for _ in range(n):
		variables.append(poisson_va_gen(media))

	return variables

def valor_p(n, sample):
	
	media = media_gen(sample)
	t_sample = estimator_gen(sample, media)
	menores = 0
	mayores = 0

	for _ in range(n):
		sample_aux = set_poisson_va_gen(len(sample), media)
		t_aux = estimator_gen(sample_aux, media)

		if (t_sample >= t_aux):
			menores += 1
		else:
			mayores += 1

	menores = menores / float(n)
	mayores = mayores / float(n)

	return 2* min(mayores, menores)

def r_gen(values, ranks):
	n = sum(values)
	result = 0

	for i in range(len(ranks)):
		result += ((ranks[i] - values[i]*(n+1)/2)**2)/float(values[i])

	result = result * 12/float((n*(n+1)))

	return result

def valor_p_ji(y, k):
	
	return 2* min(chi2.sf(y,k-1), 1 - chi2.sf(y,k-1))

val =  r_gen(valores, rangos)
print valor_p_ji(val, len(valores))