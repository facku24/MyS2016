import math

uniforms = [0.42472, 0.321111, 0.34363, 0.47426, 0.55846, 
			0.74675, 0.032061, 0.72297, 0.60431, 0.74558]

def function(t):
	return 4 / float(t +1)

def generator_homogeneo(T, lamda):
	times = []
	t = 0
	i = 0
	index = 0

	while (True):
		u = uniforms[index]
		time = - (math.log(u)/float(lamda)) 
		print time
		t += time
		if (t > T):
			break
		i += 1
		times.append(t)
		index += 1

	return times

def generator_nohomogeneo(T, f, lamda):
	t = 0
	i = 0
	index = 0
	times =[]

	while(True):
		u = uniforms[index]
		print u
		index += 1
		time = - (math.log(u)/float(lamda)) 
		print time
		t += time
		
		if (len(times) > 2 or index == 9):
			break

		u = uniforms[index]
		print u, t, f(t), f(t)/lamda
		if (u <= f(t)/lamda):
			i += 1
			times.append(t)
		
		index += 1

	return times

def generator_inversa():
	times = []
	S = 0
	i = 0

	while (i < 3):
		S += 

print generator_nohomogeneo(5, function, 4)