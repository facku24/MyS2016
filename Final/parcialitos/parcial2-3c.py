import math
from random import random

def poisson_gen(lamba, T):
	t = 0
	i = 0
	values = []
	while True:
		t += - math.log(random())/lamba
		if (t > T):
			break
		i += 1
		values.append(t)
	return values

print poisson_gen(1, 1)
