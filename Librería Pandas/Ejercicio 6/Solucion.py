import pandas as pd

def estadisticas(archivo):
	df = pd.read_csv(archivo)
	estadisticas = pd.DataFrame({
		'Mínimo': df.min(),
		'Máximo': df.max(),
		'Media': df.mean()
	})
	
	return estadisticas

archivo = 'cotizacion.csv'
resultado = estadisticas(archivo)
print(resultado)
