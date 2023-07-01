info = {}

while True:
	name = input("Introduce tu nombre: ")
	edad = input("Introduce tu edad: ")
	genero = input("Introduce tu genero: ")
	movil = input("Introduce tu número de telefono: ")
	correo = input("Introduce tu correo electrónico: ")

	info["Nombre"] = name
	info["Edad"] = edad
	info["Genero"] = genero
	info["Teléfono"] = movil
	info["Correo"] = correo

	print("Contenido actual del diccionario: ")
	for clave, valor in info.items():
		print(clave + ": " + valor)

	opcion = input("¿Deseas añadir más información? (s/n): ")
	if opcion.lower() != "s":
		break
