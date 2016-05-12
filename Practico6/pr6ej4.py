from random import normalvariate
from random import random
from scipy.special import ndtr ndtri #ndtr me da la acumulada, la otra es la inversa. Para los alphas!
import math

#The integrate value is 1.46265 aprox.
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
    desv_stand = math.sqrt(S)
    print (2*(1.96*(math.sqrt(S/float(j)))))
    while (2*(1.96*(math.sqrt(S/float(j)))) > desv_stand):
        j += 1
        X = generacion_n()
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    return M, j, S

def generacion_n():
    count = 1
    u_prev = random()
    while(True):
        print "perv: ",u_prev
        u_actual = random()
        if (u_prev > u_actual):
            print "actual: ", u_actual
            return count + 1
        count += 1
        u_prev = u_actual
    
def promedio():
    count = 0
    for _ in range(10):
        print generacion_n()
    #M , j, S = experimento(1000)
    #    count += M
    #return M, j, S

#print(promedio())
promedio()
