import matplotlib.pyplot as plt
import pandas as pd
import os

def generar(ventas, titulo, archivo):
	plt.figure(figsize=(8, 8))
	plt.pie(ventas, labels=ventas.index, autopct='%1.1f%%', startangle=140)
	plt.title(titulo)
	plt.axis('equal')
    
	plt.savefig(archivo)
	plt.close()

trimestre = pd.Series([900, 200, 600], index=['Junio', 'Julio', 'Agosto'])
diagrama = "Ventas del Trimestre"
nombre = "diagrama_ventas_trimestre.png"

generar(trimestre, diagrama, nombre)
