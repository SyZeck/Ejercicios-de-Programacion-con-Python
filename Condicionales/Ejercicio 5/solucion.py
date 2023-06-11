edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if edad >= 16 :
	if ingresos >= 1000 :
		print("Tienes que tributar.")
	else :
		print("Cuentas con la edad para tributar, pero no con los ingresos mensuales suficientes." )
else :
	print("No cuentas con la edad legal para tributar.")