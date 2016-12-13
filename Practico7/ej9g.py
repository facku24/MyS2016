#This example uses recursion to calculate p
mu2 = [6.53, 12.50, 4.34, 7.69, 12.41, 14.79, 11.02, 15.52, 43.40, 13.14]
mu1 = [6.98, 9.66, 3.53, 8.92, 12.9, 18.18, 15.56, 13.46, 42.25, 12.33]
mu1.sort()
mu2.sort()
muestra1 = [132, 104, 162, 171, 129]
muestra2 = [107, 94, 136, 99, 114, 122, 108, 130, 106, 88]
muestra1.sort()
muestra2.sort()

def rango(muestra, simulacion):
	rango = 0
	index = 0

	muestra_total = muestra + simulacion
	muestra_total.sort()

	for elem in muestra:
		while True:
			if (muestra_total[index] == elem):
				rango += index + 1
				break
			else:
				index+=1
	return rango

def recursion(n, m, r):

	#Condiciones de frontera
	if (n > 1 and m == 0):
		return 0
	if (n == 0 and m > 1):
		return 0
	if (n == 1 and m == 0):
		if (r <= 0):
			return 0
		else:
			return 1
	elif (n == 0 and m == 1):
		if (r < 0):
			return 0
		else:
			return 1
	#Condiciones recursivas
	else:
		value1 = n / float(n+m)
		value2 = m / float(n+m)
		return value1 * recursion(n-1, m, r-n-m) + value2 * recursion(n, m-1, r)

def algoritmo_recursivo(n, m, t):
	p = {}

	for i in range(0, n+1):
		for j in range(0, m+1):
			for k in range(0, t+1):
				p[i, j, k] = 0

	#inicializaciones
	for i in range(1, n+1):
		for k in range(i * (i + 1)/2, t+1):
			p[i, 0, k] = 1

	for k in range(1, t+2):
		for j in range(1, m+1):
			p[0, j, k-1] = 1

	for i in range(1, n+1):
		for j in range(1, m+1):
			for k in range(1, t+1):
				if (k < i+j):
					p[i, j, k] = (j/float(i+j)) * p[i, j-1, k]
				else:
					value1 = (i / float(i+j))
					value2 = (j / float(i+j))
					p[i, j, k] =  value1 * p[i-1, j, k-i-j] +  value2 * p[i, j-1, k]

	if (p[n, m, t] < 1-p[n, m, t-1]):
		return 2*p[n, m, t]
	else:
		return 2*(1-p[n, m, t-1])

print(algoritmo_recursivo(5, 10, 55))
#print(recursion(5, 10, 55))
print algoritmo_recursivo(10, 10, 103)