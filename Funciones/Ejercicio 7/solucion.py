def CuadradoN(numeros) :
	cuadrado = [n**2 for n in numeros]
	return cuadrado

numeros = [0,1,2,3,4,5,6,7,8,9,10]

cuad = CuadradoN(numeros)

print(f"El cuadrado de los siguientes números {numeros} es: {cuad}")




	