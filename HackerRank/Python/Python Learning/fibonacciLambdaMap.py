cube = lambda x: x[-1] + x[-2]

def fibonacci(n,l=[0,1]):
	for i in range(2,n+1):
		next_n = l[-1] + l[-2]
		l.append(next_n)
	return l

print(cube(5))