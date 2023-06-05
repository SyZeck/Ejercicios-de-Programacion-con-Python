peso = (input("Introduce tu peso en kg: "))
estatura = (input("Introduce tu estatura en metros: "))

imc = round(float(peso) / float(estatura)**2,2)

print(f"Tu indice de masa corporal es: {imc}.")