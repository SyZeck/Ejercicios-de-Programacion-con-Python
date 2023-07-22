from urllib import request
import gzip

def Pib(url, pais="ES"):

	try:
		with request.urlopen(url) as f:
			data = gzip.decompress(f.read())
			datos = data.decode('utf-8').split('\n')
	except request.URLError:
		return '¡La URL ' + url + ' no existe!'
	else:
		datos = [i.split('\t') for i in datos]  # Dividir cada línea por el tabulador
		datos = [list(map(str.strip, i)) for i in datos]  # Eliminar espacios en blanco
		for i in datos:
			i[0] = i[0][-2:]  # Obtener el código del país de los dos últimos caracteres del primer elemento de la lista
		datos[0][0] = 'años'
		datos = {i[0]: i[1:] for i in datos}
		return {datos['años'][i]: datos[pais][i] for i in range(len(datos['años']))}

pais = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', pais)
print("Año\tPIB")
for i, j in Pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true", pais).items():
    print(i, '\t', j)
