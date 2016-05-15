from random import random
import math
import sys

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

def reparacion_2(sanas, repuestos, Tf, Tr):
    #----------------------------------------------
	#----------------Inicializacion----------------

	time        = 0 	        #tiempo actual
	en_rep      = 0		        #maquinas en reparacion
	t_rep_1     = float('inf')	#tiempo en reparacion de operario 1
	t_rep_2     = float('inf')  #tiempo en reparacion de operario 2
	list_var    = []		    #lista con mis variables

	#Generamos el listado de las variables exponenciales
	#y luego las ordenamos
	for _ in range(sanas):
		list_var.append(- math.log(random())/float(Tf))

	list_var.sort()
	list_var.append(t_rep_1)
	list_var.append(t_rep_2)

	#----------------Fin Inicializacion----------------
	#--------------------------------------------------

	while (True):
		print list_var
		if (list_var[0] < t_rep_1 and list_var[0] < t_rep_2):
			
			time   = list_var[0] #actualizamos el tiempo de descomp
			list_var.remove(time)
			en_rep += 1 # We have another more 

			if (en_rep == repuestos + 1):
				return time

			if (en_rep < repuestos + 1):
				# X representa el tiempo que va a demorar
				# la nueva maq de repuesto
				X = - (math.log(random()) / float(Tf))
				list_var.append(X+time)
				print "NEW REPUEST: ", X+time
				list_var.sort()

			if (en_rep == 1):
				Y = - (math.log(random()) / float(Tr))
				t_rep_1 = time + Y

			if (en_rep == 2):
				Y = - (math.log(random()) / float(Tr))

				if (t_rep_1 == float('inf')):
					t_rep_1 = time + Y

				elif (t_rep_2 == float('inf')):
					t_rep_2 = time + Y
			print "CASO 1: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			sys.stdin.read(1)
		elif (t_rep_1 <= list_var[0] and list_var[0] < t_rep_2):
			
			time = t_rep_1
			en_rep -= 1

			if (en_rep > 1):
				Y = - math.log(random()) / float(Tr)
				t_rep_1 = time + Y

			if (en_rep == 0 or en_rep ==1):
				t_rep_1 = float('inf')
			
			print "CASO 2: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			sys.stdin.read(1)
		
		elif (t_rep_2 <= list_var[0] and list_var[0] < t_rep_1):
			
			time = t_rep_2
			en_rep -= 1

			if (en_rep > 1):
				Y = - math.log(random()) / float(Tr)
				t_rep_2 = time + Y

			if (en_rep == 0 or en_rep == 1):
				t_rep_2 = float('inf')

			print "CASO 3: time= "+ str(time) + " T1= " + str(list_var[0]) + " T2*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			sys.stdin.read(1)
		sys.stdin.read(1)
def un_operario(n):
	result = 0
	for _ in range(n):
		result += reparacion(5, 2, 1, 8)
		#reparacion(6, 4, 1, 1)
	print result / float(n)

def dos_operarios(n):
	result = 0
	for _ in range(n):
		result += reparacion_2(5, 2, 1, 8)
	print result / float(n)

def un_repuesto_mas(n):
	result = 0
	for _ in range(n):
		result += reparacion(5, 4, 1, 8)
		#reparacion(6, 4, 1, 1)
	print result / float(n)

#un_operario(1000)
#un_repuesto_mas(1000)
dos_operarios(1)