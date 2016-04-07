import random
import math

def sumatoria(n):
	resultado = 0
	lim_sup = 10000

	for _ in range(n):
		u = random.random()
		k = int(lim_sup*u) + 1
		resultado += math.e**u 
		#resultado += math.e**(k/lim_sup)

	print resultado

sumatoria(1000)