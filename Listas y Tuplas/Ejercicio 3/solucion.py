materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificacion = []

for materia in materias:
    calif = input(f"Introduce tu calificación que obtuviste en {materia}: ")
    calificacion.append(calif)

print("Las calificaciones son las siguientes:")
for i in range(len(materias)):
    print(f"En {materias[i]} obtuviste {calificacion[i]}")
