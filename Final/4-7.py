from random import random

def ej4_7():
	contador = 0
	resultados = [0,0,0,0,0,0,0,0,0,0,0]
	while (sum(resultados) < 11):
		U1 = int(6 * random()) + 1
		U2 = int(6 * random()) + 1
		resultados[U1 + U2 - 2] = 1
		contador += 1
	return contador

def repet(n):
	contador = 0
	for _ in range(n):
		contador += ej4_7()
	print contador/float(n) 

repet(1000)