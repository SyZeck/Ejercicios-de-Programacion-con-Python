numero = int(input("Introduce un número entero positivo: "))

numero = numero+1
for i in range(1, numero+1) :
	print(numero-i, end=",")