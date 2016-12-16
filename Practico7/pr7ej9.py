import math
from random import random
from scipy.stats.distributions import chi2
#valores = [0.76, 1.95, 1.62, 0.75, 0.75, 0.36, 2.23, 1.21, 0.88, 0.31, 0.39, 0.80, 0.3, 0.32, 0.92]
#valores = []

def generador_values_expo():
	values = []
	for _ in range(15):
		values.append(- math.log(random()))
	return values

valores = generador_values_expo()
#print valores

def generador_media():
	#valores = [1.6,10.3,3.5,13.5,18.4,7.7,24.3,10.7,8.4,4.9,7.9,12.,16.2,6.8,14.7]
	media = sum(valores)
	media = media/len(valores)
	return media

def generator_exp_values(n, media):
	#values = [1.6,10.3,3.5,13.5,18.4,7.7,24.3,10.7,8.4,4.9,7.9,12.,16.2,6.8,14.7]
	valores.sort()
	values_f 	= []
	for i in valores:
		values_f.append(1 - math.e**(-i/float(media)))
	return values_f

def generator_unif_values(n):
	values = []
	for _ in range(n):
		values.append(random())
	values.sort()
	return values

def generator_steps(n):
	steps = []
	for i in range(n+1):
		steps.append(i/float(n))
	return steps

def d_generator(n):
	values = generator_exp_values(n, generador_media())
	steps = generator_steps(n)
	max_global = 0
	for i in range(n):
		max_local = max(steps[i+1] - values[i], values[i] - steps[i])
		max_global = max(max_local, max_global)
	return max_global

def u_generator(n):
	values = generator_unif_values(n)
	steps = generator_steps(n)
	max_global = 0
	for i in range(n):
		max_local = max(steps[i+1] - values[i], values[i] - steps[i])
		max_global = max(max_local, max_global)
	return max_global

def valor_p(n, iterations):
	d = d_generator(n)
	print "d: ", d
	p_value = 0

	for _ in range(iterations):
		D = u_generator(n)
		if (D >= d):
			p_value += 1

	return p_value / float(iterations)

print "media: ", generador_media()
print valor_p(15, 10000)
