import pandas as pd

def calcular(df, meses):
	df_filtrado = df[df['Mes'].isin(meses)]

	balance = df_filtrado['Ventas'].sum() - df_filtrado['Gastos'].sum()

	return balance

datos = {
	"Mes": ["Enero", "Febrero", "Marzo", "Abril"],
	"Ventas": [30500, 35600, 28300, 33900],
	"Gastos": [22000, 23400, 18100, 20700]
}

df = pd.DataFrame(datos)

meses_indicados = ["Enero", "Marzo", "Abril"]

resultado = calcular(df, meses_indicados)
print("El balance total en los meses indicados es de:", resultado)
