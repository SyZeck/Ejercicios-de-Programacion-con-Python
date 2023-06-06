correo = input("Introduce tu correo electronico: ")

sustituir=correo.find("@")

nuevo=correo[:sustituir]+"@ceu.es"

print(nuevo)