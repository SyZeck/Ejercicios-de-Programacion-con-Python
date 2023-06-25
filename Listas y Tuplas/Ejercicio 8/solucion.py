cont_1 = 0

palabra = input("Introduce una palabra: ")

for ind in reversed(range(0, len(palabra))):
    if palabra[ind].lower() == palabra[cont_1].lower():
        cont_1 += 1

if len(palabra) == cont_1:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")
