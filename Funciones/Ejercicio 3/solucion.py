def NumF(numero) :
	facto = 1
 
	for i in range(1, numero+1):
    		facto = facto * i

	print(facto)
 
numero = int(input("Introduce un número entero positivo: "))

NumF(numero)