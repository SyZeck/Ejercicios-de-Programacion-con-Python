cantidad = int(input("¿Cuanto dinero tienes depositado en tu cuenta de ahorros: "))

interes = float(cantidad/4)

Uno = cantidad+interes

print(f"La cantidad ahorrada en el primer año es: {Uno}.")

interes_2 = float(Uno/4)

Dos = Uno+interes_2

print(f"La cantidad ahorrada en el segundo año es: {Dos}.")

interes_3 = float(Dos/4)

Tres = Dos+interes_3

print(f"La cantidad ahorrada en el tercer año es: {Tres}.")