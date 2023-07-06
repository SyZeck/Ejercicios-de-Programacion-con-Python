def AreaCir(radio) :
	Area_Cir = 3.1416 * (radio **2)
	return Area_Cir

def AreaCil(radio, altura) :
	Area_Cir = AreaCir(radio)
	Area_Cil = (2*Area_Cir) + (2*3.1416*radio*altura)
	return Area_Cil

radio = int(input("Introduce el valor de el radio: "))
altura = int(input("Introduce el valor de la altura: "))

Area_Cil = AreaCil(radio, altura)

print(f"El area del Cilindo es: {Area_Cil}.")