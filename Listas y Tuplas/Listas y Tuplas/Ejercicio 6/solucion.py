materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificacion = []

for materia in materias:
	calif = int(input(f"Introduce tu calificación que obtuviste en {materia}: "))
	calificacion.append(calif)

for i in range(len(materias)):
	if calificacion[i] < 70 :
		print(f"Has reprobado la materia {materias[i]}. Tendras que recursarla.")
