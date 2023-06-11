edad =int(input("Introduce la edad del cliente: "))

if edad < 4:
	print("La entrada es gratis. ")

elif 4 <= edad <= 18 :
	print("La entrada cuesta: 5$.")
else :
	print("La entrada cuesta: $10.")