import requests

def Contar(url) :
	try :
		respuesta = requests.get(url)
        
		if respuesta.status_code == 200 :
			contenido = respuesta.text

			palabras = contenido.split()
			numero = len(palabras)
            
			print("El número de palabras en el archivo es:", numero)
		else :
			print("Error al acceder al archivo. Código de estado:", respuesta.status_code)
            
	except requests.exceptions.RequestException as e :
		print("Error de conexión:", str(e))

url = str(input("Introduce la url del fichero en internet que deseas contar el número de palabras"))


Contar(url)
