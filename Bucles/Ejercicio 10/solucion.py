validar = int(input("Introduce un número entero: "))

if validar < 2 :
	primo = False
else :
	primo = True
	for i in range(2, validar) :
		if validar % i == 0 :
			primo = False
			break

if primo :
	print(f"El numero {validar} es primo.")
else :
	print(f"El numero {validar} no es primo.")