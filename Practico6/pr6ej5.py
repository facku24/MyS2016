from random import normalvariate
from random import random
import math

def experimento(stop_value):
	X = generacion_n()
	M = X
	S = 0.
	for j in range(2, 1000):
		X = generacion_n()
		A = M
		M += (X - M) / float(j)
		S = (1. - 1./(j - 1)) * S + j * (M - A)**2
	j = 1000
	while (math.sqrt(S/float(j)) > 0.01):
		j += 1
		X = generacion_n()
		A = M
		M += (X - M) / float(j)
		S = (1. - 1./(j - 1)) * S + j * (M - A)**2
	return M, j, S
  
def promedio():
    count = 0
    M , j, S = experimento(1000)
    return 4 * M, j, S

def generacion_n():
	X = 2 * random() - 1
	Y = 2 * random() - 1
	if ((X**2 + Y**2) < 1):
		return 1
	return 0

print(promedio())

