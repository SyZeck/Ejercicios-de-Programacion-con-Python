puntuacion= float(input("Introduce la puntuación del empleado: "))

bono = 2400
bono = puntuacion * bono
a = "Inaceptable"
b = "Aceptable"
c = "Meritorio"

if puntuacion == 0.0 :
	print (f"La puntuación del empleado es {a}.")
	print (f"El bono del empleado es: {bono}.")
elif puntuacion == 0.4 :
	print (f"La puntuación del empleado es {b}.")
	print (f"El bono del empleado es: {bono}.")
elif puntuacion>= 0.6 :
	print (f"La puntuación del empleado es {c}.")
	print (f"El bono del empleado es: {bono}.")

else :
	print ("El valor de la puntuación del empleado es incorrecto.")


