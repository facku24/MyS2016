import math
from random import random
from scipy.stats.distributions import chi2


def gen_conjunto(valores):
    nuevo_conjunto = []
    for _ in range(len(valores)):
        index = int(len(valores) * random())
        nuevo_conjunto.append(valores[index])
    return nuevo_conjunto


def gen_media(conjunto):
    media = sum(conjunto)
    media = media/float(len(conjunto))

    return media


def ej3():
    iteraciones = 1000
    counter = 0
    # Primero calculamos su media
    valores = [.615, 0.622, 0.631, 0.617, 0.617, 0.620, 0.621, 0.620, 0.627, 0.611]
    media = gen_media(valores)

    # Iteramos una cantidad grande de veces
    for i in range(iteraciones):
        conjunto = gen_conjunto(valores)
        media_aux = gen_media(conjunto)
        #print media, media_aux
        if (abs(media_aux - media) < 0.01):
            counter += 1
    return counter / float(iteraciones)


def ej4():
    tiradas = 101
    N = [48, 35, 15, 3]
    P = [.67, .05, .11, .17]
    T = 0
    
    for i in range(4):
        print T
        T += (N[i] - tiradas * P[i])**2 / float(tiradas * P[i])
    
    return T, chi2.sf(T, 3)

