Fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")

separador= "/"

fecha_separada= Fecha.split(separador)

print(f"El dia de tu fecha de nacimiento es: {fecha_separada[0]}.")

print(f"El mes de tu fecha de nacimiento es: {fecha_separada[1]}.")

print(f"El año de tu fecha de nacimiento es: {fecha_separada[2]}.")

