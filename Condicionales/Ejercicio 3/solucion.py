numero_1 = int(input("Introduce un dividendo: "))
numero_2 = int(input("Introduce un divisor: "))

if numero_2==0 :
	print("Error, el divisor es 0.")
else :
	division = numero_1 / numero_2
	print(f"El resultado de la operación es: {division}.")