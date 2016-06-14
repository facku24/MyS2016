from te2_pagerank import *
from grafos import *
from random import random
import time

def next_step2(n):
	counter = 0
	step = 1/float(n)
	limit = step
	ran = random()
	while (ran > limit):
		counter += 1
		limit += step
	return counter

def next_step(row):
	sort_row = row
	index = 0
	ran = random()
	counter = sort_row[0]

	while (counter < ran):
		index += 1
		counter += sort_row[index]

	return index

def estacionaridad(graph, n, rank, alfa):
	size = len(graph)
	next_index = int(size*random())
	counters = []

	if rank:
		matrix = g2p_pagerank(graph, alfa)
	else:
		matrix = g2p(graph)

	#inicializamos el arreglo contadores
	for _ in range(size):
		counters.append(0)

	# Camino n pasos
	for _ in range(n):
		row = matrix[next_index] 		#siguiente columna de nodos
		next_index = next_step(row)		#siguiente nodo a visitar
		counters[next_index] += 1

	for i in range(size):
		counters[i] = counters[i]/float(n)
	return counters

def time_to_cross(graph, rank, alfa):
	counters = []		# Los tiempos para cada nodo
	next_index = -1
	counter = 0

	if (rank):
		matrix = g2p_pagerank(graph, alfa)
	else:
		matrix = g2p(graph)

	for i in range(len(graph)):
		counters.append(0)

	# Para cada nodo, realizo la caminata
	for i in range(len(graph)):
		row = matrix[i]					# Vemos los nodos vecinos
		next_index = next_step(row)
		counter += 1					# Damos un nuevo paso

		while(next_index == i):			# Que el paso no sea a si mismo
			row = matrix[next_index]
			next_index = next_step(row)

		while(next_index != i):			# Hasta no pasar de nuevo
			row = matrix[next_index]
			next_index = next_step(row)
			counter += 1

		# Registramos los resultados
		counters[i] = counter-1		# Restamos uno a los pasos dados
		counter = 0
		# Reseteamos la variable index
		next_index = -1

	return counters

def time_to_cover(graph, rank, alfa):
	'''
	Tiempo de cubrimiento de un grafo.
	'''
	sumatory = []
	counter_t = []
	sumatory_t = len(graph)
	counter = 0

	if (rank):
		matrix = g2p_pagerank(graph, alfa)
	else:
		matrix = g2p(graph)

	for _ in range(sumatory_t):
		sumatory.append(0)
		counter_t.append(0)

	# Realizamos el recorrido desde cada nodo
	for i in range(sumatory_t):
		sumatory[i] = 1
		next_index = i
		
		#Empezamos a caminar hasta recorrero todos los nodos
		while (sum(sumatory) != sumatory_t):
			row = matrix[next_index]			#obtengo los nodos vecinos
			if (len(row) == 0 or (len(row) == 1 and row[0] == next_index)):
				counter = 0
				break
			next_index = next_step(row)		#obtengo el nodo siguiente
			sumatory[next_index] = 1
			counter += 1

		#sumo la cantidad de pasos en esta iteracion
		counter_t[i] += counter
		
		#reseteo todas las variables
		counter = 0
		sumatory = []
		for _ in range(sumatory_t):
			sumatory.append(0)
	
	return counter_t

def time_to_cover2(graph, rank, alfa):
	'''
	Tiempo de cubrimiento de un grafo.
	'''
	sumatory = []
	counter_t = []
	sumatory_t = len(graph)
	counter = 0

	if (rank):
		matrix = g2p_pagerank(graph, alfa)
	else:
		matrix = g2p(graph)

	for _ in range(sumatory_t):
		sumatory.append(0)
		counter_t.append(0)

	# Realizamos el recorrido desde un nodo aleatorio
	i = int(random() * sumatory_t)
	sumatory[i] = 1
	next_index = i
	
	#Empezamos a caminar hasta recorrero todos los nodos
	while (sum(sumatory) != sumatory_t):
		row = matrix[next_index]			#obtengo los nodos vecinos
		if (len(row) == 0 or (len(row) == 1 and row[0] == next_index)):
			counter = 0
			break
		next_index = next_step(row)		#obtengo el nodo siguiente
		sumatory[next_index] = 1
		counter += 1

	return counter

def page_adder(graph, num_pag):
	new_node = len(graph)
	for _ in range(num_pag):
		graph += ((new_node,),)

	return graph

def hacker(graph, k):
	new_node = len(graph)
	new_graph = ()
	indexed = []
	
	while (len(indexed) <= k):
		var = int(new_node*random())
		if not (var in indexed):
			indexed.append(var)

	indexed.sort()
	print indexed, len(indexed)
	
	for i in range(new_node):
		if (i in indexed):
			new_graph += (graph[i] + (new_node,),)
		else:
			new_graph += (graph[i],)

	new_graph += ((new_node,),)
	
	return new_graph

def ej1(graph, n, rank, alfa):

	print estacionaridad(graph, n, rank, alfa)

def ej2(graph, n, rank, alfa):
	counter_t = []

	for _ in range(len(graph)):
		counter_t.append(0)

	# Repetimos la simulacion n veces
	for i in range(n):
		result = time_to_cross(graph, rank, alfa)

		for i in range(len(graph)):
			counter_t[i] += result[i]

	# Obtenemos el promedio de todas las simulaciones
	for i in range(len(graph)):
		counter_t[i] = counter_t[i] / float(n)

	print counter_t

def ej3(graph, n, rank, alfa):
	result = 0

	# Repetimos la simulacion n veces
	for i in range(n):
		result += time_to_cover2(graph, rank, alfa)

	# Obtenemos el promedio de todas las simulaciones
	result = result / float(n)

	return result

def ej5a(graph, k):
	graph = page_adder(graph, k)
	counter = []

	for i in range(16):
		counter.append(0)

	for i in range(100):
		result = estacionaridad(graph)

		for i in range(len(result)):
			counter[i] += result[i]

	for i in range(16):
		counter[i] = counter[i]/float(100)
	
	return counter

def ej5b(graph, k):
	graph = hacker(graph)
	counter = []

	for i in range(len(graph)):
		counter.append(0)

	for i in range(100):
		result = estacionaridad(graph)
		for i in range(len(result)):
			counter[i] += result[i]

	for i in range(len(graph)):
		counter[i] = counter[i]/float(100)
	
	return counter
#------- EJERCICIO 1 -------
print hacker(G1, 5)
# ej1(G1, 100, False, 0)
# ej1(G1, 100, True, 0.85)
#------- EJERCICIO 2 -------
# ej2(G1, 10, False, 0)
# ej2(G1, 10, True, 0.85)
# print " "
# ej2(G2, 10, False, 0)
# ej2(G2, 10, True, 0.85)

#------- EJERCICIO 3 -------
# print "ej3(G1, 100, True, 0.05)", ej3(G1, 100, True, 0.05)
# print "ej3(G1, 100, True, 0.15)", ej3(G1, 100, True, 0.15) 
# print "ej3(G1, 100, True, 0.25)", ej3(G1, 100, True, 0.25)
# print "ej3(G1, 100, True, 0.35)", ej3(G1, 100, True, 0.35)
# print "ej3(G1, 100, True, 0.45)", ej3(G1, 100, True, 0.45)
# print "ej3(G1, 100, True, 0.55)", ej3(G1, 100, True, 0.55)
# print "ej3(G1, 100, True, 0.65)", ej3(G1, 100, True, 0.65)
# print "ej3(G1, 100, True, 0.75)", ej3(G1, 100, True, 0.75)
# print "ej3(G1, 100, True, 0.85)", ej3(G1, 100, True, 0.85)
# print "ej3(G1, 100, True, 0.95)", ej3(G1, 100, True, 0.95)
# print "ej3(G1, 100, False, 0)", ej3(G1, 100, False, 0)
# print " "
# print "ej3(G2, 100, True, 0.05)", ej3(G2, 100, True, 0.05)
# print "ej3(G2, 100, True, 0.15)", ej3(G2, 100, True, 0.15)
# print "ej3(G2, 100, True, 0.25)", ej3(G2, 100, True, 0.25)
# print "ej3(G2, 100, True, 0.35)", ej3(G2, 100, True, 0.35)
# print "ej3(G2, 100, True, 0.45)", ej3(G2, 100, True, 0.45)
# print "ej3(G2, 100, True, 0.55)", ej3(G2, 100, True, 0.55)
# print "ej3(G2, 100, True, 0.65)", ej3(G2, 100, True, 0.65)
# print "ej3(G2, 100, True, 0.75)", ej3(G2, 100, True, 0.75)
# print "ej3(G2, 100, True, 0.85)", ej3(G2, 100, True, 0.85)
# print "ej3(G2, 100, True, 0.95)", ej3(G2, 100, True, 0.95)
# print "ej3(G2, 100, False, 0)", ej3(G2, 100, False, 0)
#------- EJERCICIO 4 -------
# print "ej3(g3a, 100, False, 0)", ej3(g3a, 100, False, 0)
# print "ej3(g3b, 100, False, 0)", ej3(g3b, 100, False, 0)
# print "ej3(g3c, 100, False, 0)", ej3(g3c, 100, False, 0)
# print "ej3(g3d, 100, False, 0)", ej3(g3d, 100, False, 0)
# print "ej3(g4a, 100, False, 0)", ej3(g4a, 100, False, 0)
# print "ej3(g4b, 100, False, 0)", ej3(g4b, 100, False, 0)
# print "ej3(g4c, 100, False, 0)", ej3(g4c, 100, False, 0)
# print "ej3(g4d, 100, False, 0)", ej3(g4d, 100, False, 0)
# print "ej3(g5a, 100, False, 0)", ej3(g5a, 100, False, 0)
# print "ej3(g5b, 100, False, 0)", ej3(g5b, 100, False, 0)
# print "ej3(g5c, 100, False, 0)", ej3(g5c, 100, False, 0)
# print "ej3(g5c, 100, False, 0)", ej3(g5d, 100, False, 0)
# print "ej3(g6a, 100, False, 0)", ej3(g6a, 100, False, 0)
# print "ej3(g6b, 100, False, 0)", ej3(g6b, 100, False, 0)
# print "ej3(g6c, 100, False, 0)", ej3(g6c, 100, False, 0)
# print "ej3(g6d, 100, False, 0)", ej3(g6d, 100, False, 0)
# print "ej3(g7a, 100, False, 0)", ej3(g7a, 100, False, 0)
# print "ej3(g7b, 100, False, 0)", ej3(g7b, 100, False, 0)
# print "ej3(g7c, 100, False, 0)", ej3(g7c, 100, False, 0)
# print "ej3(g7d, 100, False, 0)", ej3(g7d, 100, False, 0)
# print "ej3(g8a, 100, False, 0)", ej3(g8a, 100, False, 0)
# print "ej3(g8b, 100, False, 0)", ej3(g8b, 100, False, 0)
# print "ej3(g8c, 100, False, 0)", ej3(g8c, 100, False, 0)
# print "ej3(g8d, 100, False, 0)", ej3(g8d, 100, False, 0)
# print "ej3(g9a, 100, False, 0)", ej3(g9a, 100, False, 0)
# print "ej3(g9b, 100, False, 0)", ej3(g9b, 100, False, 0)
# print "ej3(g9c, 100, False, 0)", ej3(g9c, 100, False, 0)
# print "ej3(g9d, 100, False, 0)", ej3(g9d, 100, False, 0)
# print "ej3(g10a, 100, False, 0)", ej3(g10a, 100, False, 0)
# print "ej3(g10b, 100, False, 0)", ej3(g10b, 100, False, 0)
# print "ej3(g10c, 100, False, 0)", ej3(g10c, 100, False, 0)
# print "ej3(g10d, 100, False, 0)", ej3(g10d, 100, False, 0)
# print "ej3(g11a, 100, False, 0)", ej3(g11a, 100, False, 0)
# print "ej3(g11b, 100, False, 0)", ej3(g11b, 100, False, 0)
# print "ej3(g11c, 100, False, 0)", ej3(g11c, 100, False, 0)
# print "ej3(g11d, 100, False, 0)", ej3(g11d, 100, False, 0)
# print "ej3(g12a, 100, False, 0)", ej3(g12a, 100, False, 0)
# print "ej3(g12b, 100, False, 0)", ej3(g12b, 100, False, 0)
# print "ej3(g12c, 100, False, 0)", ej3(g12c, 100, False, 0)
# print "ej3(g12d, 100, False, 0)", ej3(g12d, 100, False, 0)
# print ""ej3(g12a, 100, False, 0)
#------- EJERCICIO 5 -------
#print ej5a(G1, 6)
#print ej5b(G1, 10)