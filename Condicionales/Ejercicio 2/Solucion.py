contraseña= "contraseña"

valor = input("Introduce la contraseña: ")
valor_lower=valor.lower()

if valor_lower==contraseña :
	print ("La contraseña es correcta")

else:
	print("Las contraseñas no coinciden")