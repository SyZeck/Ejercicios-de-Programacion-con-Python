abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

abc_3 = [letra for indice, letra in enumerate(abc, start=1) if indice % 3 != 0]


print(abc_3)
