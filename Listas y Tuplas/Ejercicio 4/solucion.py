ganadores = []
cantidad = int(input("¿Cuantos numero son ganadores?"))

for i in range(cantidad) :
	ganador = int(input("Introduce los números ganadores de la lotería primitivar: "))
	ganadores.append(ganador)

ganadores.sort()

print("Los números ganadores de menor a mayor son: ")

for ganador in ganadores :
	print(ganador)

