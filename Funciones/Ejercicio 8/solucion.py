def EcuaV(numeros) :
	a = len(numeros)
	med = sum(numeros) / a
	var = sum((x - med) ** 2 for x in numeros) / a
	des = (var) ** 0.5
	
	valores = {
		"media" : med ,
		"varianza" : var ,
		"desviacion" : des
	}

	return valores

numeros = [0,1,2,3,4,5,6,7,8,9,10]

valores = EcuaV(numeros)

print(f"La media de {numeros} es: {valores['media']}")
print(f"La varianza de {numeros} es: {valores['varianza']}")
print(f"La desviación típica de {numeros} es: {valores['desviacion']}")

