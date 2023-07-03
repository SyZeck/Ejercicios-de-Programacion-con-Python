facturas = {}

while True:
	i = int(input("¿Desea añadir una nueva factura [1], pagar una existente [2] o terminar [3]?: "))
    
	if i == 1:
		x = str(input("Introduce el número de la nueva factura que deseas agregar: "))
		valor = float(input("Introduce el valor de coste de la factura que agregó: "))
		facturas[x] = valor
	elif i == 2:
		x = str(input("Introduce el número de la factura que desea pagar: "))
		if x in facturas:
			del facturas[x]
		else:
			print("La factura que introdujo no existe.")
	elif i == 3:
		break
	else:
		print("Opcion incorrecta.")
    
	cobrado = sum(facturas.values())
	cobrar = 0
    
	for factura in facturas.values():
		cobrar += factura
    
	print("Cantidad cobrada hasta el momento:", cobrado)
	print("Cantidad pendiente de cobro:", cobrar)
