def aplica_iva(base, iva=21):
    total = base + (base * iva / 100)
    return total

try:
    base = float(input("Introduce la base imponible de la factura: "))
    iva = float(input("Introduce el porcentaje de IVA (por defecto 21): "))

    total_factura = aplica_iva(base, iva)
    print("El total de la factura con IVA es: ", total_factura)

except ValueError:
    print("Error: Asegúrate de ingresar valores numéricos válidos para la base y el IVA.")
