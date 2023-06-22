print("Para salir del programa tienes que introducir la palabra 'salir'.")

while True :
	datos = input("Escribe cualquie palabra: ")
	if datos.lower() == "salir" :
		break
	print(datos)