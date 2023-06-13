numero = int(input("Introduce un numero entero: "))

for a in range(1, numero + 1, 2) :
	for b in range(a, 0, -2) :
		print(b, end=" ")
	print("")
