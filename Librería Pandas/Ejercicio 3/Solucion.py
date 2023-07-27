import pandas as pd

def notas_aprobados(notas, nota_aprobacion=5.0):
	notas_serie = pd.Series(notas)

	notas_aprobados_serie = notas_serie[notas_serie >= nota_aprobacion]
	notas_aprobados_serie = notas_aprobados_serie.sort_values(ascending=False)

	return notas_aprobados_serie

notas = {
	"Juana": 8.5,
	"Mario": 9.0,
	"Laura": 7.0,
	"Ana": 8.0,
	"Carlos": 9.5,
	"Pedro": 4.5,
	"Sofía": 6.0
}

resultado = notas_aprobados(notas)
print(resultado)
