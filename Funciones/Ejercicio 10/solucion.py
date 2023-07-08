def DecBin(numero):
	binario = 0
	multiplicador = 1

	while numero != 0:
		binario = binario + numero % 2 * multiplicador
		numero //= 2
		multiplicador *= 10

	return binario

def BinDec(binario):
	decimal = 0

	for posicion, digito_string in enumerate(binario[::-1]):
		decimal += int(digito_string) * 2 ** posicion

	return decimal

numero_decimal = int(input("Introduce el número Decimal que quieres convertir en número Binario: "))
numero_binario = input("Introduce el número Binario que quieres convertir en número Decimal: ")

decimal_a_binario = DecBin(numero_decimal)
binario_a_decimal = BinDec(numero_binario)

print(f"El número Decimal {numero_decimal} en Binario es: {decimal_a_binario}")
print(f"El número Binario {numero_binario} en Decimal es: {binario_a_decimal}")
