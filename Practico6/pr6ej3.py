from random import normalvariate
from random import random
import math

#e is 2.718281828459045 aprox.
def experimento(stop_value):
    lista = []
    X = generacion_n()
    M = X
    lista.append(X)
    S = 0.
    for j in range(2, stop_value):
        X = generacion_n()
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    j = stop_value
    value = 2*(1.96*(math.sqrt(S/float(j))))
    interval = (M - value, M + value)
    return S, interval

def generacion_n():
    count = 1
    result = random()
    while(result < 1):
        result += random()
        count += 1
    return count
    
def promedio():
    varianza, intervalo = experimento(1000)
    return varianza, intervalo

print(promedio())
