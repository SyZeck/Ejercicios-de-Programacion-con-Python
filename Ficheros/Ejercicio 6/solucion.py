import os

def Crear() :
    if not os.path.exists('listin.txt') :
        with open('listin.txt', 'w') as file :
            pass

def Consultar(nombre) :
    with open('listin.txt', 'r') as file:
        for line in file :
            nombre_cliente, telefono = line.strip().split(',')
            if nombre_cliente.lower() == nombre.lower() :
                return telefono
    return "Cliente no encontrado"

def Agregar(nombre, telefono) :
    with open('listin.txt', 'a') as file:
        file.write(f"{nombre},{telefono}\n")
    print("Teléfono agregado correctamente.")

def Eliminar(nombre) :
    with open('listin.txt', 'r') as file:
        lines = file.readlines()
    with open('listin.txt', 'w') as file:
        for line in lines:
            nombre_cliente, telefono = line.strip().split(',')
            if nombre_cliente.lower() != nombre.lower() :
                file.write(line)
    print("Teléfono eliminado correctamente.")

# Función principal del programa
def Gestionar() :
    Crear()
    
    while True:
        print("\n--- MENU ---")
        print("1. Consultar teléfono de un cliente")
        print("2. Agregar teléfono de un nuevo cliente")
        print("3. Eliminar teléfono de un cliente")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if opcion == "1" :
            nombre = input("Ingrese el nombre del cliente: ")
            telefono = Consultar(nombre)
            print(f"Teléfono de {nombre}: {telefono}")
        elif opcion == "2" :
            nombre = input("Ingrese el nombre del nuevo cliente: ")
            telefono = input("Ingrese el teléfono del nuevo cliente: ")
            Agregar(nombre, telefono)
        elif opcion == "3" :
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            Eliminar(nombre)
        elif opcion == "4" :
            break
        else :
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
Gestionar()
