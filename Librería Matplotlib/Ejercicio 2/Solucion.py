import matplotlib.pyplot as plt

def generar(notas, color):
	asignaturas = list(notas.keys())
	calificaciones = list(notas.values())

	plt.bar(asignaturas, calificaciones, color=color)
	plt.xlabel('Asignatura')
	plt.ylabel('Nota')
	plt.title('Notas de las asignaturas')
	plt.grid(True)
	plt.show()


notas = {
	'Matemáticas': 7.5,
	'Historia': 9.2,
	'Ciencias': 6.0,
	'Idiomas': 4.8,
	'Literatura': 10.0
}

color = 'purple'  

generar(notas, color)
