divisas = {
	'Euro':'€', 
	'Dollar':'$', 
	'Yen':'¥'
}

buscar = input("¿Qué divisa quieres que te muestre?: ")

if buscar in divisas :
	valor = divisas[buscar]
	print(F"El simbolo de la divisa {buscar} es: {valor}.")
else :
	print("La divisa que buscas no se encuentra en el diccionario.")
