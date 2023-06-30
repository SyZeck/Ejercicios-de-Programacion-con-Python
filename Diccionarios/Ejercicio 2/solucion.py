valores = {
	"Name" : "a",
	"Edad" : 1, 
	"Dirección" : "test",
	"Teléfono" : 8120	

}

primero = str(input("Introduce tu nombre: "))
segundo = int(input("Introduce tu edad: "))
tercero = str(input("Introduce tu dirección: "))
cuarto = int(input("Introduce tu numero de télefono: "))

valores["Name"] = primero
valores["Edad"] = segundo
valores["Dirección"] = tercero
valores["Teléfono"] = cuarto

nombre = valores["Name"]
edad = valores["Edad"]
direccion = valores["Dirección"]
telefono = valores["Teléfono"]

print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}.")
