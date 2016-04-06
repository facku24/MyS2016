import random

def barajada():
	baraja = []
	lst_posicion = 99
	
	for i in range(100):
		baraja.append(i+1)
	
	while (lst_posicion > 2):
		uniforme = random.random()
		new_posicion = int(lst_posicion * uniforme) +1

		# Aca swapeamos las posiciones de las cartas
		auxiliar = baraja[new_posicion]
		baraja[new_posicion] = baraja[lst_posicion]
		baraja[lst_posicion] = auxiliar

		lst_posicion -=1

	return baraja

def experimento():
	
	exitos = 0
	baraja = barajada()
	
	for i in range(100):
		if baraja[i] == i-1:
			exitos += 1
	
	return exitos

def varios_experimentos(n):

	resultado = 0
	
	for i in range(n):
		resultado += experimento()
	
	print resultado/float(n)
	
varios_experimentos(10)
varios_experimentos(100)
varios_experimentos(1000)

