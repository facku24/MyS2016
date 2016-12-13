import numpy as np
import math
import scipy.stats as st

def estimador_normal(n, m, r):
	numerador = r - n * (n+m+1)/float(2)
	value = numerador / float(math.sqrt(n*m*(n+m+1)/float(12)))
	normal = st.norm()
	#return 2* (1-normal.cdf(value))
	return 2 * (normal.cdf(value))

#print(estimador_normal(5, 10, 55))
print(estimador_normal(10, 10, 103))