producto= input("Introduce el nombre del producto: ") 
precio= float(input("Introduce el precio del producto: "))
unidades= int(input("Introduce el numero de unidades del producto: "))

total= precio * unidades

imprimir=(f"El producto es: {producto}\n")
imprimir+=(f"El precio unitario es: {precio:0>8.2f}\n")
imprimir+=(f"El numero de unidades es: {unidades:0>3}\n")
imprimir+=(f"El costo total es: {total:0>10.2f}")

print(imprimir)
