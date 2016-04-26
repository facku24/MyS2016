
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import random
import math

def ej2(n,p):
	U = random()
	i = 0
	c = p / float(1 - p)
	Pr = (1 - p) ** n
	F = Pr
	while U >= F:
		Pr = (c*(n-i)/float(i+1))*Pr
		F += Pr
		i = i + 1
	return i


def ej3a(lamda, fun_lamda, T):
	t = 0
	i = 0
	S = [0]
	U = random()
	t -= (1/float(lamda)) * math.log(U)
	while t <= T:
		V = random()
		if V < fun_lamda(t)/float(lamda):
			i += 1
			S.append(t)
		U = random()
		t -= (1/float(lamda)) * math.log(U)
	return S, i

def fun_lamda(t):
	return (1 + 1 / float(1+t))


def ej3b(lamda, fun_lamda, T):
	t = 0
	j = 0
	i = 0
	S = [0]
	T1 = 0.5
	T2 = 1.
	while true:
	U = random()
	X = -(1/float(lamda))* math.log(U)	
	while t + X > tj:
		if (j == k+1): 
			break
		X = (X-tj+t)*fun_lamda(j)/float(lamda)
		t = tj
		j = j+1
	t = t + X
	V = random()
	if V < fun_lamda(t)/float(lamda):
		i = i+1
		S.append(t)


