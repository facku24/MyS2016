from random import random
import math

def experimento(n, Tf, Tr, repuestos):
	time = 0
	en_rep = 0
	t_rep  = float('inf')
	list_var = []

	#Generamos el listado de las variables exponenciales
	#y luego las ordenamos
	for _ in range(n):
		list_var.append(- math.log(random())/float(Tf))
	list_var.sort()

	list_var.append(t_rep)

	while (True):

		#caso t1 < t*
		if (list_var[0] < t_rep):
			time   = list_var[0] #actualizamos el tiempo de descomp
			en_rep += 1 # We have another more 
			if (en_rep == repuestos):
				return time
			if (en_rep < repuestos + 1):
				# X representa el tiempo que va a demorar la nueva maq
				# en reparacion
				X = - math.log(random()) / float(Tr)
				list_var.append(X+time)
				list_var.sort()
			if (en_rep == 1):
				Y = - math.log(random()) / float(Tf)
				t_rep = time + Y
		#caso t* <= t1
		elif (t_rep <= list_var[0]):
			time = t_rep
			en_rep -= 1
			if (r > 0):
				# Y = tiempo de reparacion de la nueva maquina
				Y = - math.log(random()) / float(Tf)
				t_rep = time + Y
			if (en_rep == 0):
				t_rep = float('inf')

def promedio(n):
	result = 0
	for _ in range(n):
		result += experimento(6, 1, 1, 4)
	print result / float(n)

promedio(4000)