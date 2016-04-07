from random import random

def experimento(n):
	
	suma_1 = 0
	suma_2 = 0
	
	for _ in range(n):
		X = lanzamientos()
		suma_1 += X
		suma_2 += X**2
	
	esperanza = suma_1 / float(n)
	varianza = suma_2/float(n) - esperanza**2
	
	print esperanza, varianza

def lanzamientos():
		lanzamientos = 0
		lanzamientos_restantes = 11
		sumas_posibles=[]

		for _ in range(11):
			sumas_posibles.append(0)

		while (lanzamientos_restantes > 0):
			U = random()
			V = random()
			dado1 = int(U*6)+1
			dado2 = int(V*6)+1
			suma_actual = dado1 + dado2

			if (sumas_posibles[suma_actual-2] == 0):
				sumas_posibles[suma_actual-2] = 1
				lanzamientos_restantes -= 1
			lanzamientos += 1
		
		return lanzamientos

experimento(100)
experimento(1000)
experimento(10000)
experimento(100000)
