import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

df['Survived'].value_counts().plot(kind='pie', labels=['Fallecidos', 'Supervivientes'],autopct='%1.1f%%', startangle=90, figsize=(6, 6))
plt.title('Fallecidos y Supervivientes')
plt.axis('equal')
plt.show()

df['Age'].plot(kind='hist', bins=20, edgecolor='black', figsize=(8, 6))
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades')
plt.grid(True)
plt.show()

df['Pclass'].value_counts().sort_index().plot(kind='bar', edgecolor='black', figsize=(8, 6))
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Número de Personas en cada Clase')
plt.grid(axis='y')
plt.show()

df.groupby(['Pclass', 'Survived']).size().unstack().plot(kind='bar', edgecolor='black', stacked=True, figsize=(8, 6))
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Número de Personas Fallecidas y Supervivientes en cada Clase')
plt.grid(axis='y')
plt.legend(['Fallecidos', 'Supervivientes'])
plt.show()

mddf['Survived'].replace({0: 'Fallecidos', 1: 'Supervivientes'}).groupby(df['Pclass']).value_counts().unstack().plot(kind='bar', edgecolor='black', stacked=True, figsize=(8, 6))
plt.xlabel('Clase')
plt.ylabel('Número de Personas')
plt.title('Número de Personas Fallecidas y Supervivientes Acumuladas en cada Clase')
plt.grid(axis='y')
plt.legend(['Fallecidos', 'Supervivientes'])
plt.show()
