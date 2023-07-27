import pandas as pd
import numpy as np
from datetime import datetime

def cargar_datos():
	filenames = ["emisiones-2016.csv", "emisiones-2017.csv", "emisiones-2018.csv", "emisiones-2019.csv"]
	dfs = [pd.read_csv(filename) for filename in filenames]

	df = pd.concat(dfs)

	return df

def reestructurar(df):
	df = df[['ESTACION', 'MAGNITUD', 'AÑO', 'MES', 'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09',
		'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30', 'D31']]

	df = pd.melt(df, id_vars=['ESTACION', 'MAGNITUD', 'AÑO', 'MES'], var_name='DIA', value_name='EMISION')

	df['FECHA'] = pd.to_datetime(df['AÑO'].astype(str) + '-' + df['MES'].astype(str) + '-' + df['DIA'].str.strip('D').astype(str), errors='coerce')

	df = df.dropna(subset=['FECHA'])
	df = df.sort_values(by=['ESTACION', 'FECHA'])

	return df

def mostrar(df):
	estaciones = df['ESTACION'].unique()
	contaminantes = df['MAGNITUD'].unique()

	print("Estaciones disponibles:", estaciones)	
	print("Contaminantes disponibles:", contaminantes)

def emisiones_por_estacion_contaminante_fecha(df, estacion, contaminante, fecha_inicio, fecha_fin):
	df_filtrado = df[(df['ESTACION'] == estacion) & (df['MAGNITUD'] == contaminante) & (df['FECHA'] >= fecha_inicio) & (df['FECHA'] <= fecha_fin)]

	return df_filtrado[['FECHA', 'EMISION']]

def resumen_descriptivo_contaminantes(df):
	resumen = df.groupby('MAGNITUD')['EMISION'].describe()

	return resumen

def resumen_descriptivo_contaminantes_por_distrito(df):
	resumen = df.groupby(['MAGNITUD', 'ESTACION'])['EMISION'].describe()

	return resumen

def resumen_descriptivo_estacion_contaminante(df, estacion, contaminante):
	df_filtrado = df[(df['ESTACION'] == estacion) & (df['MAGNITUD'] == contaminante)]
	resumen = df_filtrado['EMISION'].describe()

	return resumen

def emisiones_medias_mensuales(df, contaminante, año):
	df_filtrado = df[(df['MAGNITUD'] == contaminante) & (df['AÑO'] == año)]

	emisiones_medias = df_filtrado.groupby('MES')['EMISION'].mean()

	return emisiones_medias

def medias_mensuales_contaminantes_por_estacion(df, estacion):
	df_filtrado = df[df['ESTACION'] == estacion]

	medias_mensuales = df_filtrado.groupby(['MAGNITUD', 'MES'])['EMISION'].mean()

	return medias_mensuales

def main():
	df = cargar_datos()
	df = reestructurar_dataframe(df)

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
	
	mostrar_estaciones_y_contaminantes(df)

	datos_pasajero_148 = df.loc[df.index == 147]
	print("\nDatos del pasajero con identificador 148:")
	print(datos_pasajero_148)

	filas_pares = df.iloc[::2]
	print("\nFilas pares del DataFrame:")
	print(filas_pares)

	emisiones = emisiones_por_estacion_contaminante_fecha(df, 'nombre_estacion', 'nombre_contaminante', 'fecha_inicio', 'fecha_fin')
	print("\nEmisiones en la estación y rango de fechas dados:")
	print(emisiones)

	resumen_contaminantes = resumen_descriptivo_contaminantes(df)
	print("\nResumen descriptivo para cada contaminante:")
	print(resumen_contaminantes)

	resumen_contaminantes_por_distrito = resumen_descriptivo_contaminantes_por_distrito(df)
	print("\nResumen descriptivo para cada contaminante por distrito:")
	print(resumen_contaminantes_por_distrito)

	resumen_estacion_contaminante = resumen_descriptivo_estacion_contaminante(df, 'nombre_estacion', 'nombre_contaminante')
	print("\nResumen descriptivo para la estación y contaminante dados:")
	print(resumen_estacion_contaminante)

	emisiones_medias_mensuales_contaminante = emisiones_medias_mensuales(df, 'nombre_contaminante', 'año')
	print("\nEmisiones medias mensuales del contaminante y año dados:")
	print(emisiones_medias_mensuales_contaminante)

	medias_mensuales_contaminantes_por_estacion = medias_mensuales_contaminantes_por_estacion(df, 'nombre_estacion')
	print("\nMedias mensuales de los distintos contaminantes por estación:")
	print(medias_mensuales_contaminantes_por_estacion)

if __name__ == "__main__":
    main()
