import csv

def Leer(archivo):
    Estudiantes = []
    with open(archivo, newline='') as leer:
        reader = csv.DictReader(leer)
        for row in reader:
            Estudiantes.append({
                'Apellidos': row['Apellidos'],
                'Nombre': row['Nombre'],
                'Asistencia': float(row['Asistencia']),
                'Parcial1': float(row['Parcial1']),
                'Parcial2': float(row['Parcial2']),
                'Practicas': float(row['Practicas']),
            })
    return sorted(Estudiantes, key=lambda x: x['Apellidos'])


def Final(Estudiantes):
    for student in Estudiantes:
        parcial1_weight = 0.3
        parcial2_weight = 0.3
        practicas_weight = 0.4
        final = (student['Parcial1'] * parcial1_weight) + (student['Parcial2'] * parcial2_weight) + (student['Practicas'] * practicas_weight)
        student['Nota_Final'] = final


def Separar(Estudiantes):
    Aprobado = []
    Reprobado = []
    for student in Estudiantes:
        attendance_threshold = 0.75
        exam_threshold = 4
        final_grade_threshold = 5

        if (student['Asistencia'] >= attendance_threshold and
            student['Parcial1'] >= exam_threshold and
            student['Parcial2'] >= exam_threshold and
            student['Practicas'] >= exam_threshold and
            student['Nota_Final'] >= final_grade_threshold):
            Aprobado.append(student)
        else:
            Reprobado.append(student)

    return Aprobado, Reprobado
