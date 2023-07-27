import pandas as pd

def estadisticas(notas):
	notas_serie = pd.Series(notas)

	nota_minima = notas_serie.min()
	nota_maxima = notas_serie.max()
	nota_media = notas_serie.mean()
	nota_desviacion_tipica = notas_serie.std()

	estadisticas = pd.Series({
		"Mínima": nota_minima,
		"Máxima": nota_maxima,
		"Media": nota_media,
		"Desviación Típica": nota_desviacion_tipica
	})

	return estadisticas

notas = {
	"Pedro": 8.5,
	"Ana": 9.0,
	"Javier": 7.0,
	"Juana": 8.0,
	"Londres": 9.5
}

resultado = estadisticas(notas)
print(resultado)
