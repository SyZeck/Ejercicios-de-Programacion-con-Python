def Tabla(n) :
	try :
		with open (f"tabla-{n}.txt",'r') as archivo :
			tabla = archivo.read()
			print(tabla)
	except FileNotFoundError :
		print("El archivo tabla-{n}.txt no existe")

n = int(input("Introduce un número entero entre 1 y 10: "))
while n <1 or n>10 :
	print("Debe introducir un número entero entre 1 y 10")
	n = int(input("Introduce un número entero entre 1 y 10: "))

Tabla(n)