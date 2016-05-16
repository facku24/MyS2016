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
	bins = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
	
	plt.hist(result, bins, histtype='bar', rwidth=0.8)
	plt.xlabel('x')
	plt.ylabel('y')
	#plt.title('Sistema de Lavanderia')
	plt.legend()
	plt.show
	#print result

def ejemplo():
	mu, sigma = 100, 15
	x = mu + sigma * np.random.randn(10000)

	# the histogram of the data
	n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


	plt.xlabel('Smarts')
	plt.ylabel('Probability')
	plt.title('Histogram of IQ')
	plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
	plt.axis([40, 160, 0, 0.03])
	plt.grid(True)
	plt.show()

def dos_operarios(n):
	result = 0
	for _ in range(n):
		result += reparacion_2(5, 2, 1, 8)
	print result / float(n)

def un_repuesto_mas(n):
	result = 0
	for _ in range(n):
		result += reparacion(5, 3, 1, 8)
		#reparacion(6, 4, 1, 1)
	print result / float(n)

#un_operario(10000)
#un_repuesto_mas(1000)
#dos_operarios(1000)
ejemplo()