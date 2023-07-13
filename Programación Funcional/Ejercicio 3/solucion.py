def list(funcion, lista):
	resultado = []
	for i in lista:
		resultado.append(funcion(i))
	return resultado

def cuad(n):
	return n * n

print(list(cuad, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
