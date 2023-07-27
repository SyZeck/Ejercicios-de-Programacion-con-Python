import pandas as pd

def main():
	datos = {
		"Mes": ["Enero", "Febrero", "Marzo", "Abril"],
		"Ventas": [30500, 35600, 28300, 33900],
		"Gastos": [22000, 23400, 18100, 20700]
	}

	df = pd.DataFrame(datos)

	print(df)

if __name__ == "__main__":
	main()
