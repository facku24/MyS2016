from random import random
from scipy.stats.distributions import chi2


def generator(n):
	values = [0,0,0,0,0]
	for _ in range(n):
		U = int(random()*5) 
		values[U] += 1
	return values

def generator_T(values, probs):
	resultado = 0
	n       = sum(values)
	for i in range(len(values)):
		resultado += ((values[i] - n*probs[i])**2)/float(n*probs[i])
	return resultado

print generator_T([12,5,19,7,7], [0.2, 0.2, 0.2, 0.2, 0.2])
new_values = generator(50)
print new_values
print generator_T(new_values, [0.2, 0.2, 0.2, 0.2, 0.2])
#print generator(50)