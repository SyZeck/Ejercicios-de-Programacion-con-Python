import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def generar(notas):
	plt.figure(figsize=(8, 6))
	sns.boxplot(x=notas)
	plt.xlabel('Notas')
	plt.title('Distribución de notas')
	plt.show()

notas = pd.Series([9.5, 10.0, 4.5, 7.2, 9.5, 8.0, 2.8, 9.8, 6.2, 8.3, 7.9])

generar(notas)
