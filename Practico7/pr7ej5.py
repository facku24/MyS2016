import math
from scipy.stats.distributions import chi2

values = [6,7,3,4,7,2,6,3,7,8,2,1,3,5,8,7]

def estimador_p(n):
	result = 0
	for i in values:
		result += i
	return result/float((len(values))*n)

def sum_iguales(i):
	result = 0
	for j in values:
		if (j == i):
			result += 1
	return result

def nCi(n, i):
	f = math.factorial
	return f(n)/ float((f(i)*f(n-i)))

def calculate_p_i(p, n, i):
	q = 1-p
	result = nCi(n, i) * (p**i) * (q**(n-i))
	print "p_i:", i, result
	return result

def estimador(indep_vars, values_posb):
	T = 0
	p = estimador_p(values_posb)

	for i in range(values_posb + 1):
		Ni = sum_iguales(i)
		npi = indep_vars * calculate_p_i(p, values_posb, i)
		print "i:", i, " Ni: ", Ni, " npi: ", npi
		print "(Ni - npi): ", (Ni - npi), "(Ni - npi)2: ", (Ni - npi)**2
		print((Ni - npi)**2 / float(npi))
		T += (Ni - npi)**2 / float(npi)
		print "T:", T
	return T

def valor_p(T, k):
	return chi2.sf(T,k-1)

def calculate():
	T = estimador(16, 8)
	print "T: ", T
	return valor_p(T, 8)

print calculate()