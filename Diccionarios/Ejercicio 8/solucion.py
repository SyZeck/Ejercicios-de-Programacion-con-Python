idioma = input("Introduce las palabras en español e inglés separadas por dos puntos (:) y cada par separado por comas.")

idiomas = {}
duplas = idioma.split(",")

for dupla in duplas:
	palabra = dupla.split(":")
	español = palabra[0].strip()
	ingles = palabra[1].strip()
	idiomas[español] = ingles

traducir = input("Introduce una frase en español: ")

palabras = traducir.split()
traduccion = []

for palabra in palabras:
	traducida = idiomas.get(palabra, palabra)
	traduccion.append(traducida)

print("La traducción es: " + " ".join(traduccion))
