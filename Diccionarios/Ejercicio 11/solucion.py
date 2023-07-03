directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

cortar = directorio.split('\n')  
nombres = cortar[0].split(';')  
clientes = {}

for corta in cortar[1:]:
    datos = corta.split(';')  
    cliente = {}
    for i in range(len(nombres)):
        nombre = nombres[i]
        dato = datos[i]
        if nombre == 'descuento':
            dato = float(dato)
        cliente[nombre] = datos
    clientes[datos[0]] = cliente

print(clientes)
