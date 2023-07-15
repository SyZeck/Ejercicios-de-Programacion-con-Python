def Frac(frase) :
	palabras = frase.split()
	rellenar = {}
	
	for palabra in palabras :
		rellenar[palabra] = len(palabra)
	return rellenar

frase = input("Introduce una Frase: ")
imprimir = Frac(frase)
print(imprimir)