# Solo se puede mostrar el método INDEX y el COUNT

tupla = ("Rafa" , 39 , True)

print(type(tupla))

print(dir(tupla))


# INDEX

elemento_encontrado = tupla.index(39)

print(elemento_encontrado)


# COUNT

numero_elementos = tupla.count(39)

print(numero_elementos)