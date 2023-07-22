import csv

def leer_cotizaciones(fichero):
    datos = {}
    with open(fichero, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for columna in lector.fieldnames:
            datos[columna] = []
        
        for fila in lector:
            for columna in lector.fieldnames:
                datos[columna].append(fila[columna])
    
    return datos


def generar_resumen_cotizaciones(datos, fichero_resumen):
    resumen = {}
    for columna, valores in datos.items():
        valores_numericos = [float(valor) for valor in valores]
        resumen[columna] = {
            'Mínimo': min(valores_numericos),
            'Máximo': max(valores_numericos),
            'Media': sum(valores_numericos) / len(valores_numericos)
        }
    
    with open(fichero_resumen, 'w', newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['Columna', 'Mínimo', 'Máximo', 'Media'])
        escritor.writeheader()
        for columna, valores in resumen.items():
            valores['Columna'] = columna
            escritor.writerow(valores)
