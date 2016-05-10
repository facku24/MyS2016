from random import normalvariate
from random import random
import math

#The integrate value is 1.46265 aprox.
def experimento():
    lista = []
    U = random()
    X = math.exp(U**2)
    M = X
    lista.append(X)
    S = 0.
    for j in range(2, 100):
        U = random()
        X = math.exp(U**2)
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    j = 30
    while (math.sqrt(S/float(j)) > 0.01):
        j += 1
        U = random()
        X = math.exp(U**2)
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    return M, j

def promedio():
    count = 0
    for _ in range(100):
        M , j = experimento()
        count += j
    return count/float(100)

print (promedio())
