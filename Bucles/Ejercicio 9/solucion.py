contraseña = "contraseña"

while True :
	validar = input("Introduce la contraseña: ")
	if validar == contraseña : 
		print("Acceso permitido")
		break
	else :
		print("Intente nuevamente, introdujo una contraseña incorrecta")
