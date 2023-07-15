def Crear(materias, calif) :
	nuevo = {}
	
	for i in range(len(materias)) :
		materia = materias[i].upper()
		resultado = calif[i]
		nuevo[materia] = resultado
	return nuevo
		
calif = [100, 28, 89, 42,71]
materias = ['Artes', 'Geografia', 'Matematicas', 'Geografia', 'Español']

imprimir = Crear(materias, calif)

print(imprimir)