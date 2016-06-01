from random import normalvariate
from random import random
#from scipy.special import ndtr ndtri #ndtr me da la acumulada, la otra es la inversa. Para los alphas!
import math

#The value of e is 2.718281828459045 aprox
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
    u_prev = random()
    while(True):
        u_actual = random()
        if (u_prev > u_actual):
            return count + 1
        count += 1
        u_prev = u_actual
    
def promedio():
    counter = 0
    varianza, intervalo = experimento(1000)
    for _ in range(100):
        X = generacion_n()
        if intervalo[0] < X < intervalo[1]:
            counter += 1
    #return varianza, intervalo
    return counter / float(100)

print(promedio())

