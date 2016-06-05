

muestra = [342, 361, 448, 453, 504]
simulacion = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]

simulacion.sort()

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

print(rango(simulacion, muestra))
print(rango(muestra, simulacion))
