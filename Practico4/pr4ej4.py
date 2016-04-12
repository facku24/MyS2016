from random import random
import math

def metodo():
	U = random()
	Y = random()
	
	if (U < 0.5):
		X = int(math.log(Y)/math.log(0.5))+1
	else:
		X = int(math.log(Y)/math.log(2/float(3)))+1

	print X

def experimento():
	for _ in range(10):
		metodo()

experimento()