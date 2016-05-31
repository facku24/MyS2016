
values = [6,7,3,4,7,3,7,2,6,3,7,8,2,1,3,5,8,7]

def estimador(n):
	result = 0
	for i in values:
		result += i
	return result/(float(len(values))*n)

def sum_iguales(i):
	result = 0
	for j in values:
		if (j == i):
			result += 1
	return result

print estimador(8)
for i in range(0,9):
	print i, sum_iguales(i)
