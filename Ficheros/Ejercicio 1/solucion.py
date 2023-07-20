def Tabla(n) :
	with open (f"tabla-{n}.txt",'w') as archivo :
		for i in range(1,11):
			multiplicacion = n * i 
			archivo.write(f"{n} x {i} = {multiplicacion}\n") 

n = int(input("Introduce un número entero entre 1 y 10: "))
while n <1 or n>10 :
	print("Debe introducir un número entero entre 1 y 10")
	n = int(input("Introduce un número entero entre 1 y 10: "))

Tabla(n)