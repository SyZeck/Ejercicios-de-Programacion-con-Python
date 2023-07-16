def ModVect(x,y, z = None) :
	if z is None :
		modu = (x**2 + y**2) ** 0.5
	else :
		modu = (x**2 + y**2 + z**2) ** 0.5
	return modu

di = int(input("Desea calcular un vector de 2 o 3 dimensiónes?: "))
if di == 2 :
	x = int(input("Introduce el valor a del vector: "))
	y = int(input("Introduce el valor b del vector: "))
	imprimir = ModVect(x,y)
elif di == 3 :
	x = int(input("Introduce el valor a del vector: "))
	y = int(input("Introduce el valor b del vector: "))
	z = int(input("Introduce el valor c del vector: "))
	imprimir = ModVect(x,y,z)
else :
	imprimir = "Solo se admiten vectores de 2 y 3 dimensiónes."

print(imprimir)