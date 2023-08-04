import pandas as pd
import matplotlib.pyplot as plt

def generar(fichero):
	df = pd.read_csv(fichero_csv)

	empresas = df['Empresa'].unique()

	plt.figure(figsize=(10, 6))
	plt.xlabel('Fecha')
	plt.ylabel('Cotización de Cierre')
	plt.title('Series Temporales de Cotizaciones de Cierre de Bancos')

	for empresa in empresas:
		datos_banco = df[df['Empresa'] == empresa]
		plt.plot(datos_banco['Fecha'], datos_banco['Cierre'], label=empresa)

	plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
	plt.xticks(rotation=45)
	plt.grid(True)
	plt.tight_layout()
	plt.show()

generar('bancos.csv')
