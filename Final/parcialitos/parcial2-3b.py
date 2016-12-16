import math
from random import random

lambas = [0, 2 , 5/float(3)]
times = [0, 0.5, 1]
k = 1
def func_intes(x):
	return 1 + 1/float(1+x)

def adelgazamiento(lamba, T):
	t = 0
	i = 0
	j = 1
	values = []
	lamba = lambas[j]
	while True :
		x = - math.log(random())/lamba

	 	while (t + x > times[j]):
	 		if (j == k + 1):
	 			return values
 			j += 1
 			x = (x - times[j] + t)*lamba/lambas[j]
 			t = times[j]
 			lamba = lambas[j]

		t += x
		u = random()
		if (u < func_intes(t)/lamba):
			i += 1
			values.append(t)
	

	return values


print adelgazamiento(2, 1)
