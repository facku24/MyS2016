import math
from random import random
from scipy.stats.distributions import chi2

def generator_exp_values(n, media):
	values = [86,133,75,22,11,144,78,122,8,146,33,41,99]
	values.sort()
	values_f 	= []
	for i in values:
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

def d_generator(n, media):
	values = generator_exp_values(n, media)
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

def valor_p(n, media, iterations):
	d = d_generator(n, media)
	print "d: ", d
	p_value = 0

	for _ in range(iterations):
		D = u_generator(n)
		if (D >= d):
			p_value += 1

	return p_value / float(iterations)

print valor_p(13, 50, 500)