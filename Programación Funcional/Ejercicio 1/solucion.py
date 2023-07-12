def aplicar_descuento(precio, descuento):
	descontado = precio - (precio * descuento / 100)
	return descontado

def aplicar_iva(precio):
	iva = 0.16
	total = precio * (1 + iva)
	return total

def calcular_precio_final(cesta, funcion):
	final = 0
	for producto, precio in cesta.items():
		final += funcion(precio)
	return final

productos = {}
descuentos = {}

while True:
	producto = input("Introduce el nombre del producto o escribe 'salir' si no deseas agregar otro producto: ")
    
	if producto.lower() == 'salir':
		break
    
	precio = float(input("Introduce el precio del producto: "))
	descuento = float(input("Introduce el descuento del producto: "))
    
	productos[producto] = precio
	descuentos[producto] = descuento

cesta = productos.copy()

print("La cesta de la compra es: ")
for producto, precio in cesta.items():
	print(producto + ": $" + str(precio))

opcion = input("¿Deseas aplicar descuento (D) o IVA (I) a los productos de la cesta? ")
if opcion.lower() == 'd':
	precio_final = calcular_precio_final(cesta, lambda precio: aplicar_descuento(precio, descuentos[producto]))
	print("Precio final de la cesta con descuento: $" + str(precio_final))
elif opcion.lower() == 'i':
	precio_final = calcular_precio_final(cesta, aplicar_iva)
	print("Precio final de la cesta con IVA: $" + str(precio_final))
else:
	print("Opción no válida.")



