import pandas as pd

def calcular(ventas):
    return ventas * 0.9

def main():
    inicio = int(input("Ingresa el año inicial: "))
    fin = int(input("Ingresa el año final: "))
    
    ventas = pd.DataFrame(columns=["Año", "Ventas"])

    for año in range(inicio, fin + 1):
        ventas_año = float(input(f"Ingrese las ventas para el año {año}: "))
        ventas = pd.concat([ventas, pd.DataFrame({"Año": [año], "Ventas": [ventas_año]})], ignore_index=True)

    ventas["Ventas con descuento"] = calcular(ventas["Ventas"])

    print("\nDatos originales de ventas por año:")
    print(ventas)

if __name__ == "__main__":
    main()

