from random import random
import math

def reparacion(sanas, repuestos, Tf, Tr):
	#---------Inicializacion

	time = 0 		        #tiempo actual
	en_rep = 0		        #maquinas en reparacion
	t_rep  = float('inf')	#tiempo en reparacion
	list_var = []		    #lista con mis variables

	#Generamos el listado de las variables exponenciales
	#y luego las ordenamos
	for _ in range(sanas):
		list_var.append(- math.log(random())/float(Tf))
	list_var.sort()
	list_var.append(t_rep)
	#print("lista original: ", list_var)

	#--------Fin Inicializacion

	while (True):
		#print "ENTRADA AL CICLO"
		#print "en reparacion: ", en_rep
		if (list_var[0] < t_rep):
			#print "falla una nueva"
			time   = list_var[0] #actualizamos el tiempo de descomp
			list_var.remove(time)
			en_rep += 1 # We have another more 
			if (en_rep == repuestos + 1):
				#print "TIEMPO: ", time
				return time
			if (en_rep < repuestos + 1):
				# X representa el tiempo que va a demorar
				# la nueva maq de repuesto
				X = - (math.log(random()) / float(Tf))
				#print "tiempo del resp: ", X+time
				list_var.append(X+time)
				list_var.sort()
				#print "nueva lista: ", list_var
			if (en_rep == 1):
				Y = - (math.log(random()) / float(Tr))
				t_rep = time + Y
				#print "tiempo en reparacion: ", t_rep
		#caso t_rep <= t1
		elif (t_rep <= list_var[0]):
			time = t_rep
			en_rep -= 1
			if (en_rep > 0):
				# Y = tiempo de reparacion de la nueva maquina
				Y = - math.log(random()) / float(Tr)
				t_rep = time + Y
				#print "tiempo en reparacion2: ", t_rep
			if (en_rep == 0):
				t_rep = float('inf')

def un_operario(n):
	result = 0
	for _ in range(n):
		result += reparacion(5, 2, 1, 8)
		#reparacion(6, 4, 1, 1)
	print result / float(n)

def un_repuesto_mas(n):
	result = 0
	for _ in range(n):
		result += reparacion(5, 4, 1, 8)
		#reparacion(6, 4, 1, 1)
	print result / float(n)

un_operario(10000)
un_repuesto_mas(10000)
