import pandas as pd

def main():
	df = pd.read_csv('titanic.csv')

	print("Dimensiones del DataFrame:", df.shape)
	print("Número de datos en el DataFrame:", df.size)
	print("\nNombres de las columnas:")
	print(df.columns)
	print("\nNombres de las filas (índices):")
	print(df.index)
	print("\nTipos de datos de las columnas:")
	print(df.dtypes)
	print("\nLas 10 primeras filas:")
	print(df.head(10))
	print("\nLas 10 últimas filas:")
	print(df.tail(10))

	print("\nDatos del pasajero con identificador 148:")
	print(df.loc[147])

	print("\nFilas pares del DataFrame:")
	print(df.iloc[::2])

	print("\nNombres de personas en primera clase ordenados alfabéticamente:")
	print(df[df['Pclass'] == 1]['Name'].sort_values())

	print("\nPorcentaje de personas que sobrevivieron:")
	print(df['Survived'].value_counts(normalize=True) * 100)

	print("\nPorcentaje de personas que sobrevivieron en cada clase:")
	print(df.groupby('Pclass')['Survived'].mean() * 100)

	df = df.dropna(subset=['Age'])

	print("\nEdad media de mujeres en cada clase:")
	print(df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean())

	df['Menor de edad'] = df['Age'] < 18

	print("\nPorcentaje de menores de edad que sobrevivieron en cada clase:")
	print(df[df['Menor de edad']]['Survived'].groupby(df['Pclass']).mean() * 100)

	print("\nPorcentaje de mayores de edad que sobrevivieron en cada clase:")
	print(df[~df['Menor de edad']]['Survived'].groupby(df['Pclass']).mean() * 100)

if __name__ == "__main__":
	main()
