frase=input("Introduce una frase: ")
vocal= input("Introduce una vocal en minuscula: ")

vocal_mayus = vocal.upper()
nueva= frase.replace(vocal, vocal_mayus)

print(nueva)