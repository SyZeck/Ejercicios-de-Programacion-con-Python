completo = {"clientes": {}, "datos": {}}

while True:
	i = int(input("¿Desea añadir un nuevo cliente [1], eliminar un cliente [2], mostrar los datos de un cliente [3], listar todos los clientes [4], listar los clientes preferentes [5] o terminar [6]?: "))

	if i == 1:
		x = str(input("Introduce el NIF del nuevo cliente que deseas agregar sus datos: "))
		name = input("Introduce el nombre del cliente: ")
		dire = input("Introduce la dirección del cliente: ")
		movil = input("Introduce el número de teléfono del cliente: ")
		correo = input("Introduce el correo electrónico del cliente: ")
		prefe = input("Introduce si el cliente es preferente (True / False): ")
        
		completo["clientes"][x] = x
		completo["datos"][x] = {
		"Nombre": name,
		"Dirección": dire,
		"Teléfono": movil,
		"Correo": correo,
		"Preferente": prefe
		}
    
	elif i == 2:
		x = str(input("Introduce el NIF del cliente que deseas eliminar sus datos: "))
		if x in completo["clientes"]:
			del completo["clientes"][x]
			del completo["datos"][x]
		else:
			print("El NIF que introdujo no existe.")
    
	elif i == 3:
		x = str(input("Introduce el NIF del cliente que deseas mostrar sus datos: "))
		if x in completo["datos"]:
			print(completo["datos"][x])
		else:
			print("El NIF que introdujo no existe.")
    
	elif i == 4:
		for nif, cliente in completo["datos"].items():
			print("NIF:", nif)
			for dato, valor in cliente.items():
				print(dato + ":", valor)
			print()
    
	elif i == 5:
		for nif, cliente in completo["datos"].items():
			if cliente["Preferente"] == "True":
				print("NIF:", nif)
				for dato, valor in cliente.items():
					print(dato + ":", valor)
				print()
    
	elif i == 6:
		break
    
	else:
		print("Opción incorrecta.")

	opcion = input("¿Deseas añadir más información? (s/n): ")
	if opcion.lower() != "s":
		break
