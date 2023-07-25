listin = {'Juan': 123456789, 'Pedro': 987654321}

def elimina(listin, usuario):
    if usuario in listin:
        telefono = listin[usuario]
        del listin[usuario]
        return telefono
    else:
        return None

nombre_usuario = 'Pablo'
telefono_eliminado = elimina(listin, nombre_usuario)

if telefono_eliminado is not None:
    print(f"El teléfono de {nombre_usuario} es: {telefono_eliminado}")
else:
    print(f"{nombre_usuario} no se encuentra en el listín telefónico.")
