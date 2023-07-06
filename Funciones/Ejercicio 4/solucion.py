def FactuT(cantidad, iva=None) :
	if iva is None or iva == "" :
		iva = 0.21
	else :
		iva = float(iva)

	total = cantidad * (1 + iva)
	return total

cantidad = int(input("Introduce la cantidad total sin IVA: "))
iva = input("Introduce el porcenta de IVA a aplicar(eje 0.21): ")
	
total = FactuT(cantidad, iva)
print(total)
