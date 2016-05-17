from random import random
import matplotlib.pyplot as plt
import math
import sys
import numpy as np

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
		#print list_var

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
			#	print "NEW REPUEST: ", X+time
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
			#print "CASO 1: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			#sys.stdin.read(1)

		elif (t_rep_1 < list_var[0] and t_rep_2 < list_var[0]):
			
			if (t_rep_1 <= t_rep_2):
				time = t_rep_1
				en_rep -= 1

				if (en_rep > 1):
					Y = - math.log(random()) / float(Tr)
					t_rep_1 = time + Y

				if (en_rep == 0 or en_rep ==1):
					t_rep_1 = float('inf')
				
				#print "CASO 2a: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
				#sys.stdin.read(1)

			elif (t_rep_2 < t_rep_1):
				time = t_rep_2
				en_rep -= 1

				if (en_rep > 1):
					Y = - math.log(random()) / float(Tr)
					t_rep_2 = time + Y

				if (en_rep == 0 or en_rep ==1):
					t_rep_2 = float('inf')
				
				#print "CASO 2b: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
				#sys.stdin.read(1)

		elif (t_rep_1 < list_var[0]):
			
			time = t_rep_1
			en_rep -= 1

			if (en_rep > 1):
				Y = - math.log(random()) / float(Tr)
				t_rep_1 = time + Y

			if (en_rep == 0 or en_rep ==1):
				t_rep_1 = float('inf')
			
			#print "CASO 2: time= "+ str(time) + " T1= " + str(list_var[0]) + " T1*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			#sys.stdin.read(1)
		
		elif (t_rep_2 <= list_var[0]): #and list_var[0] < t_rep_1):
			
			time = t_rep_2
			en_rep -= 1

			if (en_rep > 1):
				Y = - math.log(random()) / float(Tr)
				t_rep_2 = time + Y

			if (en_rep == 0 or en_rep == 1):
				t_rep_2 = float('inf')

			#print "CASO 3: time= "+ str(time) + " T1= " + str(list_var[0]) + " T2*= " + str(t_rep_1) + " T2*= " + str(t_rep_2)
			#sys.stdin.read(1)
		
		#sys.stdin.read(1)

def un_operario(n):
	result = []
	for _ in range(n):
		result.append(reparacion(5, 2, 1, 8))
	return result

def dos_operarios(n):
	result = []
	for _ in range(n):
		result.append(reparacion_2(5, 2, 1, 8))
	return result 

def un_repuesto_mas(n):
	result = []
	for _ in range(n):
		result.append(reparacion(5, 3, 1, 8))
	return result 

def ejemplo():
	#sist_normal = un_operario(10000)
	sist_repuesto 	= un_repuesto_mas(10000)
	#sist_doble 		= dos_operarios(10000)

	bins = np.linspace(0, 10, 40)
	#plt.hist(sist_doble, bins, histtype='bar', rwidth=0.65, color='c', edgecolor='b', label='Dos Operarios')
	#plt.hist(sist_repuesto, bins, histtype='bar', rwidth=0.65, color='g', edgecolor='none', label='Nuevo Repuesto')
	#plt.hist(sist_normal, bins, histtype='bar', rwidth=0.65, color='c',label='Sistema Actual')
	plt.hist(sist_repuesto, bins, histtype='bar', rwidth=0.65, color='c',label='Nuevo Repuesto')
	plt.xlabel('Tiempo de Falla (Meses)')
	plt.xticks(np.arange(min(bins), max(bins)+1, 1.0))
	plt.ylabel('Cantidad de Fallas')
	plt.title('Sistema de Lavanderia')
	plt.legend()
	plt.show()

ejemplo()