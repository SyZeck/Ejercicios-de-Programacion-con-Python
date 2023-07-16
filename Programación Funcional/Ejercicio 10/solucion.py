def Calcular(inmueble) :
	antiguedad = 2023 - inmueble['año']
	precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - antiguedad / 100)
	if inmueble['zona'] == 'B':
 		precio *= 1.5
	inmueble['precio'] = precio
	return precio

def Buscar(lista, presupuesto) :
	presu = []
	for inmueble in lista :
		precio = Calcular(inmueble)
		if precio <= presupuesto :
			presu.append(inmueble)
	return presu
	
lista = [
	{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
	{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
	{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
	{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
	{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = int(input("¿De cuantó es tu presupuesto?: "))

presu = Buscar(lista, presupuesto)

for inmueble in presu :
	print(f"Precio del inmueble: {inmueble['precio']}")

