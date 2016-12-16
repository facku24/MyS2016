from random import normalvariate
from random import random
from scipy.special import ndtr, ndtri 
import math

values = [4.6, 4.9, 3.2, 6.4, 4.8, 3.8, 5.7, 5.4, 4.4, 6.3]

def z(alfa):
	return - ndtri(alfa/float(2))

def estimadores(valores):
	'''
	Esta funcion calcula la media y varianza de un arreglo fijo
	pasado como parametro
	'''
	M = valores[0]
	S = 0.

	for j in range(1,len(valores)):
		elem = valores[j]
		A = M
		M += (elem - M) / float(j+1)
		S = (1. - 1./(j)) * S + (j+1) * (M - A)**2

	return M, S

def intervalo(M, S, Z, n):
	limite = Z * math.sqrt(S / n)
	print "limite: ", limite
	return (M - limite, M + limite)

Z1 = z(0.1)
print "z(0.1): ", Z1
Z2 = z(0.05)
print "z(0.05): ", Z2
media, varianza = estimadores(values)
print "media: ", media, "varianza: ", varianza
n = len(values)
print intervalo(media, varianza, Z1, n)
print intervalo(media, varianza, Z2, n)