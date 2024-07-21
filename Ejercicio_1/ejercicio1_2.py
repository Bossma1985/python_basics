

frase = input("Escribe una frase y te digo cuanto tiempo tardarías en decirla ")

palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_palabras} palabras y tardarías: {cantidad_palabras / 2} en decirlas")
print(f"Dalto tardaría: {cantidad_palabras * 100 // 2 / 1.3 / 100} segundos en decirlo")
if cantidad_palabras > 120:
    print("Hey máquina. Tampoco te pedí un testamento")

