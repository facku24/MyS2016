from random import random

muestra = [342, 361, 448, 453, 504]
simulaciones = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]

def generador_subset(n, m):
	length = n+m
	listado = muestra + simulaciones

	k = length-1

	while (k > 0):
		u = int(length * random())
		aux = listado[k]
		listado[k] = listado[u]
		listado[u] = aux
		k -= 1

	return listado[0: n]

def rango(muestra, simulaciones, subset):
	rango = 0
	index = 0

	muestra_total = muestra + simulaciones
	muestra_total.sort()

	subset.sort()
	
	for elem in subset:
		while True:
			if (muestra_total[index] == elem):
				rango += index + 1
				break
			else:
				index+=1
	return rango

def simulacion(n, t):
	p_inf = 0
	p_sup = 0

	for _ in range(n):
		subset = generador_subset(5, 10)
		r = rango(muestra, simulaciones, subset)
		if (r <= t):
			p_inf += 1
		if (r >= t):
			p_sup += 1
	value = min(p_inf/float(n), p_sup/float(n))

	return 2*value

print(simulacion(1000, 55))