def calif(notas) :
	calif = []	
	
	for nota in notas :

		if nota >= 90:
			calif.append('Artes')
		elif nota >= 80:
			calif.append('Matematicas')
		elif nota >= 70:
			calif.append('Español')
		elif nota >= 60:
			calif.append('Historia')
		else:
			calif.append('Geografia')

	return calif

notas = [100, 28, 89, 42,71]

imprmir = calif(notas)

print(imprmir)