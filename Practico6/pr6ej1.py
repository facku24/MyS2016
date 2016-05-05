from random import normalvariate
import math


def experimento():
    lista = []
    X = normalvariate(0, 1)
    M = X
    lista.append(X)
    S = 0.
    for j in range(2, 30):
        X = normalvariate(0, 1)
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    j = 30
    while (math.sqrt(S/float(j)) > 0.1):
        j += 1
        X = normalvariate(0, 1)
        lista.append(X)
        A = M
        M += (X - M) / float(j)
        S = (1. - 1./(j - 1)) * S + j * (M - A)**2
    #suma = sum(lista)
    #suma = suma/float(j)
    return M, j

def promedio():
    count = 0
    for _ in range(1000):
        M , j = experimento()
        count += j
    return count/float(1000)

print (promedio())
