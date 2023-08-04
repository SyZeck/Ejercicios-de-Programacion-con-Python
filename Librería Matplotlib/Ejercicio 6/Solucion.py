import matplotlib.pyplot as plt
import pandas as pd

def generar(df):
	plt.figure(figsize=(8, 6))
    
	meses = df.index
	ingresos = df['Ingresos']
	gastos = df['Gastos']
    
	plt.plot(meses, ingresos, label='Ingresos', marker='o', linestyle='-', color='b')
	plt.plot(meses, gastos, label='Gastos', marker='o', linestyle='-', color='r')
    
	plt.xlabel('Meses')
	plt.ylabel('Valor')
	plt.title('Evolución de ingresos y gastos')
	plt.legend()
	plt.ylim(bottom=0)  # Fijar el eje y para que empiece en 0
	plt.grid(True)
	plt.show()


datos = {
    'Ingresos': [8000, 4000, 9500, 2100, 1000, 6800],
    'Gastos': [2500, 3800, 6400, 1130, 2850, 5100]
}

meses = ['Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre']

df = pd.DataFrame(datos, index=meses)

generar(df)
