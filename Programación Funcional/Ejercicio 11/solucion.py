def Valores(muestra) :
	n = len(muestra)

	suma = 0
	for valor in muestra :
		suma += valor
	media = suma / n
	
	diferencias = 0
	for valor in muestra :
		diferencia = valor - media
	diferencias += diferencia ** 2
	
	desvia = (diferencias / n) ** 0.5

	valores = []
	for valor in muestra :
		puntua = (valor - media) /desvia
		if puntua > 3 or puntua < -3 :
			valores.append(valor)

	return valores

muestra = []
while True :
	valor = input("Ingresa los valores de muestra, o introduzca 'n' si esta la muestra completa: ")
	if valor == 'n' :
		break
	muestra.append(float(valor))

calcular = Valores(muestra)

print("Valores atípicos encontrados:")
for valor in calcular:
    print(valor)