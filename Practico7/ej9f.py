
muestra = [342, 361, 448, 453, 504]
simulacion = [186, 220, 225, 456, 276, 199, 371, 426, 242, 311]
mu2 = [6.53, 12.50, 4.34, 7.69, 12.41, 14.79, 11.02, 15.52, 43.40, 13.14]
mu1 = [6.98, 9.66, 3.53, 8.92, 12.9, 18.18, 15.56, 13.46, 42.25, 12.33]
muestra1 = [2,3,4]
muestra2 = [3,5,7]

def rango(totalset, subset):
	'''
	This function generates the rank for subset.

	param - totalset: Debe de ser el conjunto total y ordenado de todas las muestras
					  simuladas y las muestras observadas
	param - subset: Debe de ser el subconjunto al cual le quiero generar el rango
	'''
	rango = 0
	index = 0

	totalset.sort()
	subset.sort()
	
	for elem in subset:
		while True:
			if (totalset[index] == elem):
				if (index < len(totalset)-1 and totalset[index] == totalset[index+1]):
					rango += (2*index+3) /float(2)
				elif (index > 0 and totalset[index] == totalset[index-1]):
					rango += (2*index+1) /float(2)
				else:
					rango += index + 1
					index += 1
				break
			else:
				index+=1
	return rango

#print(rango(simulacion+muestra, muestra))
#print(rango(simulacion+muestra, simulacion))
#print(rango(muestra1+muestra2, muestra1))
#print(rango(muestra1+muestra2, muestra2))
print(rango(mu1+mu2, mu2))
print(rango(mu1+mu2, mu1))
