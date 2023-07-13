def calcu(calculadora='s'):
	print("Las opciones de la calculadora son las siguientes: ")
	print("1. Seno")
	print("2. Coseno")
	print("3. Tangente")
	print("4. Exponencial")
	print("5. Logaritmo Neperiano")
	elegir = int(input("¿Qué opción desea utilizar?: "))
	valor = int(input("Introduce el valor entero que deseas utilizar: "))

	print("Número | Resultado")
	for n in range(1, valor + 1):
		if elegir == 1:
			resultado = Seno(n, valor)
		elif elegir == 2:
			resultado = Coseno(n, valor)
		elif elegir == 3:
			resultado = Tangente(n, valor)
		elif elegir == 4:
			resultado = Exponencial(n, valor)
		elif elegir == 5:
			resultado = LogNep(n, valor)
		else:
			print("No seleccionaste una opción válida.")
			return

		print(n, "|", resultado)

def Seno(x, valor):
	resultado = 0.0
	signo = 1

	for n in range(1, valor + 1, 2):
		termino = (x ** n) / Fact(n)
		resultado += signo * termino
		signo *= -1

	return resultado

def Coseno(x, valor):
	resultado = 0.0
	signo = 1

	for n in range(0, valor + 1, 2):
		termino = (x ** n) / Fact(n)
		resultado += signo * termino
		signo *= -1

	return resultado

def Tangente(x, valor):
	seno = Seno(x, valor)
	coseno = Coseno(x, valor)

	if coseno == 0.0:
		return float('inf') if seno > 0 else float('-inf')
	else:
		return seno / coseno

def Exponencial(x, valor):
	resultado = 0.0

	for n in range(valor + 1):
		termino = (x ** n) / Fact(n)
		resultado += termino

	return resultado

def LogNep(x, valor):
	if x <= 0:
		return float('nan')

	resultado = 0.0

	for n in range(1, valor + 1):
		termino = (x - 1) ** n / n
		resultado += termino

	return resultado

def Fact(n):
	if n == 0:
		return 1
	else:
		return n * Fact(n - 1)

calculadora = input("¿Desea utilizar la calculadora? s/n :")
if calculadora == 'n':
	print("Entendido. Adiós n.n")
else:
	calcu()
