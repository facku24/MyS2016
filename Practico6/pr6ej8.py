from random import random
import math

def servidor(lamda_a, lamda_s):

	#Inicializacion
	tiempo 	 = 0
	cliente  = 0
	operario = float('inf')
	index 	 = 1
	en_rep 	 = 0
	C = [0]		# Lista de tiempos de clientes
	A = [0] 	# Lista de tiempos de arribos
	S = [0]		# Lista de tiempos de servicio
	V = [0]		# Lista de tiempos de salidas
	W = [0]		# Lista de tiempos de espera 

	#Algoritmo
	while(tiempo < 8):
		nuevo_cliente = - math.log(random())/float(lamda_a)
		C.append(nuevo_cliente)
		nuevo_cliente += A[index-1]

		if (nuevo_cliente < operario):
			if (cliente <= 3):
				tiempo = nuevo_cliente
				A.append(nuevo_cliente)
				S.append(- math.log(random())/float(lamda_s))
				V.append(max(A[index], V[index-1])+S[index])
				W.append(V[index]-A[index])
				cliente += 1
				index += 1
				if (cliente == 1):
					en_rep += 1
					operario = tiempo + S[en_rep]

		if (operario < nuevo_cliente):
			tiempo = operario
			A.append(nuevo_cliente)
			S.append(- math.log(random())/float(lamda_s))
			V.append(max(A[index], V[index-1])+S[index])
			W.append(V[index]-A[index])
			cliente -= 1
			index += 1
			if (cliente > 0):
				en_rep += 1
				operario = tiempo + S[en_rep]
			elif (cliente == 0):
				operario = float('inf')
	
	

	#print "   C         A         S         V         W"
	#for i in range(1,index):
	#	print round(C[i],4),"   ",round(A[i],4),"   ",round(S[i],4),"   ",round(V[i],4),"   ",round(W[i],4) 
	print "Tiempo de cierre: ",tiempo

servidor(4.0, 4.2)