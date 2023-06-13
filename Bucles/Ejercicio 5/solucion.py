cantidad = int(input("Introduce la cantidad a invertir: "))

interes= int(input("Introduce el interes anual: "))

años = int(input("Introduce el numero de años: "))

for i in range(años) :
	cantidad *= 1+ interes / 100

	print(f"El capital al pasar {i+1} años es de: {round(cantidad,2)}")