calif = {
	'Matemáticas': 6, 
	'Física': 4, 
	'Química': 5
}
total = sum(calif.values())

for x, y in calif.items() :
	print(f"{x} tiene {y} créditos.")

print(f"El número total de créditos del curso es: {total}.")