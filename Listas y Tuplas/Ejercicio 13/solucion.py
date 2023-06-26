muestra = input("Introduce una muestra de números separados por comas: ")

muestra = [float(num) for num in muestra.split(",")]

med = sum(muestra) / len(muestra)

cuadrado = sum((x - med)** 2 for x in muestra)

desvia = (cuadrado / len(muestra)) ** 0.5


print(f"La media de los números es {med}")
print(f"La deviación tipica de los números es {desvia}")
