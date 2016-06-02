import math
from random import random
from scipy.stats.distributions import chi2

def generator_exp_values(n, media):
	values = [66,72,81,94,112,116,124,140,145,155]
	values_f 	= []
	for i in values:
		values_f.append(1 - math.e**(-i/float(media)))
	values_f.sort()
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
	values = generator_exp_values(n, 100)
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
		#print "D: ", D
		if (D >= d):
			p_value += 1

	return p_value / float(iterations)

print valor_p(10, 500)