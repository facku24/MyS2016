from random import random

def lanzamiento(n):

	total = 0
	
	for _ in range(n):
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

		total += lanzamientos
		#print "Lanzamientos", lanzamientos
	print total/n

	
lanzamiento(10)
lanzamiento(100)
lanzamiento(1000)
lanzamiento(10000)
lanzamiento(100000)
