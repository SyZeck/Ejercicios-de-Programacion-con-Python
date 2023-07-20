def Tabla(n,m) :
	nombre = f"tabla-{n}.txt"
    
	try:
		with open(nombre, 'r') as fichero:
			lineas = fichero.readlines()
		print(lineas[m-1])
	except FileNotFoundError :
		print(f"El archivo tabla-{m}.txt no existe")

n = int(input("Ingrese un número entre 1 y 10: "))
m = int(input("Ingrese otro número entre 1 y 10: "))
    
if n < 1 or n > 10 or m < 1 or m > 10:
	print("Los números deben estar entre 1 y 10.")

Tabla(n,m)
