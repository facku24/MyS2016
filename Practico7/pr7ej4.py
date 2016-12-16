import math
from random import random
from scipy.stats.distributions import chi2

def f_unif(x):
	return (x - 50) /float(150)

def unif_values():
	values_f = [164, 142, 110, 153, 103, 52, 174, 88, 178, 184, 58, 62, 132, 128]
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
	values = unif_values()
	steps = generator_steps(n)
	max_global = 0
	for i in range(n):
		max_local = max(steps[i+1] - f_unif(values[i]), f_unif(values[i]) - steps[i])
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

print valor_p(14, 500)