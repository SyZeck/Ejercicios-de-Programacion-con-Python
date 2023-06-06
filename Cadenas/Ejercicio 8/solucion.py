precio = input("Introduce el precio del producto en euros con dos decimales: ")

borrar=precio.find(".")

despues=precio[borrar:]

antes=precio[:borrar]


print(f"El numero de euros del precio introducido es: {antes}")

print(f"El numero de centimos del precio introducido es: {despues}")