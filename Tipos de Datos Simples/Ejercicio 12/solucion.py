barra = 3.49
viejo = 60
descuento = barra* (viejo/100)
precio = barra - descuento

panes= int(input("Introduce el número de barras vendidas que no son del día: "))

final= round(panes*precio)

print(f"El precio habitual de una barra de pan es: {barra}$.")
print(f"El descuento  que se le hace por no ser fresca es: 60.0%.")
print(f"El coste final total es: {final}.")