u = (1, 2, 3)
v = (4, 5, 6)

def producto_escalar(u, v):
    if len(u) != len(v):
        raise ValueError("Los vectores deben tener la misma longitud.")
    
    resultado = 0
    for i in range(len(u)):
        resultado += u[i] * v[i]
    
    return resultado

print(producto_escalar(u, v))
