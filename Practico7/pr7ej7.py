import math
from random import random
from scipy.stats.distributions import chi2

values = [122, 133, 106, 128, 135, 126]
values.sort()

def generator_media():
	media = 0
	for i in values:
		media += i
	return media/float(len(values))

def func_distro_expo(x, media):
	return 1 - math.e**(-x/float(media))

def func_distro_exp_values(n, media):
	values_f 	= []
	for i in values:
		values_f.append(func_distro_expo(i, media))
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
	values = func_distro_exp_values(n, media)
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
	media = generator_media()
	print "media: ", media
	d = d_generator(n, media)
	print "d: ", d
	p_value = 0

	for _ in range(iterations):
		D = u_generator(n)
		if (D >= d):
			p_value += 1

	return p_value / float(iterations)

print valor_p(6, 500)