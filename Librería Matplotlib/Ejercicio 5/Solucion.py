import matplotlib.pyplot as plt
import pandas as pd

def generar(ventas, grafico):
	plt.figure(figsize=(8, 6))
    
	if grafico == 'lineas':
		plt.plot(ventas, ventas.values, marker='o', linestyle='-', color='b')
	elif grafico == 'barras':
		plt.bar(ventas.index, ventas.values, color='b')
	elif grafico == 'sectores':
		plt.pie(ventas, labels=ventas.index, autopct='%1.1f%%', startangle=140)
	elif grafico == 'areas':
		plt.fill_between(ventas.index, ventas.values, color='b', alpha=0.3)
	else:
		raise ValueError("Tipo de gráfico no válido. Los valores válidos son: lineas, barras, sectores, areas")
    
	plt.xlabel('Años')
	plt.ylabel('Número de ventas')
	plt.title('Evolución del número de ventas')
	plt.grid(True)
	plt.show()

ventas = pd.Series([2000, 1800, 1400, 2100], index=[2020, 2021, 2022, 2023])
grafico = str(input("¿Qué tipo de grafico desea, los graficos posibles son lineas, barras, sectores y areas?: "))

generar(ventas, grafico)
