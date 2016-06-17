from random import random
import matplotlib.pyplot as plt
import math
import sys
import numpy as np

def ejemplo():
	datos = [0.17, 0.09, 0.28, 0.15, 0.07, 0.02, 0.05, 0.08, 0.01, 0.08]
	alpha, loc, beta=5, 100, 22
	x = np.linspace(0,9) 
	h = plt.plot(x, datos, lw=2)
	plt.show()

ejemplo()