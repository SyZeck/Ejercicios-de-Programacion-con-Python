inv = float(input("Introduce la cantidad que quienres invertir: "))
inta = float(input("Introduce cual es el interés anual: "))
años = int(input("Introduce el numero de años de la inversión: "))

resul = str(round (inv*(inta / 100+1)**años,2))

print(f"El capital obtenido por la inversión es: {resul}")