def GenDic(palabra) :
	palabras = {}
	for letra in palabra.split() :
		if letra in palabras :
			palabras[letra] += 1
		else :
			palabras[letra] = 1
	return palabras

def TupFre(palabras) :
	Frecuente = ''
	contador = 0
	for keys, values in palabras.items() :
		if values > contador :
			contador = values
			frecuente = keys
	return frecuente, contador

palabra = input("Introduce una cadena de caracteres: ")

diccionario = GenDic(palabra)
frecuente, frecuencia = TupFre(diccionario)

print("El diccionario con las palabras y frecuencias es: ")
for palabra, frecuencia in diccionario.items() :
	print(f"{palabra}: {frecuencia}")

print(f"La palabra mas repetida es {frecuente}, y la frecuencia es {frecuencia}.")
