precios = {


"Plátano" : "1.35",
"Manzana" : "0.80",
"Pera" : "0.85",
"Naranja" : "0.70"

}

fruta = str(input("¿Qué fruta desea?: "))

if fruta in precios :
	kilos = int(input("¿Cuántos kilos de la fruta desea?"))
else :
	print("La fruta que buscas no se encuentra en el diccionario.")

if fruta in precios :
	valor = float(precios[fruta])
	costo = valor * kilos
	print(f"El precio de {kilos} kilos de {fruta} es: {costo}")


