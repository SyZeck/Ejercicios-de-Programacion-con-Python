def MaxD(a,b) :
	while b != 0 :
		a, b = b, a %b 
	return a

def MinC(a,b) :
	maximo = MaxD(a,b)
	minimo = (a*b) // maximo
	return minimo	

x =int(input("Introduce el primer valor: "))
y =int(input("Introduce el segundo valor: "))

maximo = MaxD(x,y)
minimo = MinC(x,y)

print("El MCD de", x, "y", y, "es: ",maximo)  
print("El MCM de", x, "y", y, "es: ",minimo)  





