contar = input("Introduce una palabra: ")

contar_a = contar_e = contar_i = contar_o = contar_u = 0

for letra in contar:
	letra = letra.lower()
	if letra == 'a':
		contar_a += 1
	elif letra == 'e':
		contar_e += 1
	elif letra == 'i':
		contar_i += 1
	elif letra == 'o':
		contar_o += 1
	elif letra == 'u':
		contar_u += 1


print(f"La vocal 'a': {contar_a}")
print(f"La vocal 'e': {contar_e}")
print(f"La vocal 'i': {contar_i}")
print(f"La vocal 'o': {contar_o}")
print(f"La vocal 'u': {contar_u}")
