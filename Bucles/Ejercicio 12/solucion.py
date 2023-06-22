frase = str(input("Introduce una frase: "))
repetir = str(input("Introduce una letra: "))
contar = 0

for letra in frase :
	if letra == repetir :
		contar += 1
print("La letra " + repetir + "se repite " + str(contar) + " veces.")

