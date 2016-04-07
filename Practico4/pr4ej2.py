#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math
#--------------------------------------------------------------
#			EJERCICIO 2  
#--------------------------------------------------------------
# Se desea construir una aproximación de 
#
#	SUM from k = 1 to N exp**(k/N)
#
# donde N = 10000
#
# a) Escribir un algoritmo para estimar la cantidad deseada
# b) Obtener la aproximaciòn sorteando 100 nùmeros aleatorios
# c) ¿Es una buena aproximación?
#--------------------------------------------------------------
#--------------------------------------------------------------

def sumatoria(n):
	resultado = 0
	lim_sup = 10000

	for _ in range(n):
		u = random.random()
		k = int(lim_sup*u) + 1
		resultado += math.e**(k/float(lim_sup))
	print lim_sup * resultado / float(n)

sumatoria(10)
sumatoria(100)
sumatoria(1000)
