meses = {
    '01': 'Enero',
    '02': 'Febrero',
    '03': 'Marzo',
    '04': 'Abril',
    '05': 'Mayo',
    '06': 'Junio',
    '07': 'Julio',
    '08': 'Agosto',
    '09': 'Septiembre',
    '10': 'Octubre',
    '11': 'Noviembre',
    '12': 'Diciembre'
}

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/') + 1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/') + 1:]

imprimir = meses[mes]

print(f"La fecha es {dia} de {imprimir} de {año}")


