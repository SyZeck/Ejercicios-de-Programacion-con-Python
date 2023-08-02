import matplotlib.pyplot as plt

def ventas_año(años):
	ventas = []
	for año in años:
		venta = float(input(f"Porfavor ingrese las ventas del año {año}: "))
		ventas.append(venta)
	return ventas

def mostrar(años, ventas):
	plt.plot(años, ventas, marker='o', linestyle='-', color='b')
	plt.xlabel('Año')
	plt.ylabel('Ventas')
	plt.title('Evolución de las ventas por año')
	plt.grid(True)
	plt.show()

def main():
	print("~Programa de seguimiento de ventas~")
	inicial = int(input("Porfavor ingrese el año inicial: "))
	final = int(input("Porfavor ingrese el año final: "))

	años = list(range(inicial, final + 1))
	ventas = ventas_año(años)
	mostrar(años, ventas)

if __name__ == "__main__":
	main()
