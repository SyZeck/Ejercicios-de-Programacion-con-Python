def lista(funcion, lista):
	l = []
	for i in lista:
		if funcion(i):
			l.append(i)
	return l

def bool(n):
	return n % 2 == 0

print(lista(bool, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

