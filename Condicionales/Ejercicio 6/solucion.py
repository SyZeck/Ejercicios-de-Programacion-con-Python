Nombre= input("Introduce tu nombre: ")
Sexo= input("Introduce tu Sexo en formato M=Mujer, H=Hombre: ")

if (Sexo == "M" and Nombre.lower() < 'm') or (Sexo == "H" and Nombre.lower() > 'n'):
    print ("Tu grupo es el grupo A")
else:
    print ("Tu grupo es el grupo B")

	