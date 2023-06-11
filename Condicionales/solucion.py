Renta= int(input("Introdue tu renta Anual: "))

if Renta > 60000 :
	porcentaje  = 45*Renta/100
	print (f"El tipo impositivo que te corresponde es de: {porcentaje}.")
elif 35000 <= Renta <= 60000 :

	porcentaje  = 30*Renta/100
	print (f"El tipo impositivo que te corresponde es de: {porcentaje}.")
elif 20000 <= Renta <= 35000 :

	porcentaje  = 20*Renta/100
	print (f"El tipo impositivo que te corresponde es de: {porcentaje}.")
elif 10000 <= Renta <= 20000 :
			
	porcentaje  = 15*Renta/100
	print (f"El tipo impositivo que te corresponde es de: {porcentaje}.")
else :

	porcentaje  = 5*Renta/100
	print (f"El tipo impositivo que te corresponde es de: {porcentaje}.")