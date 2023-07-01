productos = {}
sigue="s"
while sigue == "s" :
	producto = input("Ingresa el artículo: ")
	precio = input("Ingresa el precio del artículo: ")
	productos[producto] = precio

	opcion = input("¿Deseas añadir más información? (s/n): ")
	if opcion.lower() != "s":
		break

print("La lista de la compra es: ")
for x, y in productos.items() :
	print(f"Artículo: {x} Precio: {y}.")
