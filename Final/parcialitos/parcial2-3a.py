import math
from random import random

def func_intes(x):
	return 1 + 1/float(1+x)

def adelgazamiento(lamba, T):
	t = 0
	i = 0
	values = []
	while True :
		t += - math.log(random())/lamba
	 	if (t > T):
	 		break
		u = random()
		if (u < func_intes(t)/lamba):
			i += 1
			values.append(t)
	return values


print adelgazamiento(2, 1)
