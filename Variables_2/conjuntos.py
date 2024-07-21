# 1 Crear conjuntos con la función SET:

conjunto = set(["Rafa" , "manzana" , 33])

print("1 - Crear conjuntos con la función SET:")
print(type(conjunto))
print(conjunto)
print("-----------------------------")


# 2 Meter un conjunto dentro de otro conjunto. Para ello es necesario usar 1º la función: FROZENSET.

print("2 - Meter un conjunto dentro de otro conjunto:")

conjunto2 = frozenset([66 , "Rosa" , "Camion"])
conjunto2B = {conjunto2 , "colorama"}
print(type(conjunto2))
print(conjunto2B)
print("-----------------------------")


# 3 CONJUNTOS y SUBCONUNTOS:

print("3 CONJUNTOS y SUBCONUNTOS:")


conjunto3 = {1, 3, 5, 7}
conjunto3B = {11, 31, 51,}

print(type(conjunto3))
print(conjunto3)

# ISSUBSET: Verificar si es un subconjunto. Hay 2 formas de hacerlo:

# 1º Con método issubset.

print("1 - Verificar si es un subconjunto:")

resultado1 = conjunto3B.issubset(conjunto3)
print(resultado1)

# 2º Con operadores de comparación:

resultado1B = conjunto3B <= conjunto3
print(resultado1B)

# ISSUPERSET: Verificar si es un superconjunto:

# 1º con método issuperset.

print("2 - Verificar si es un superconjunto:")

resultado2 = conjunto3.issuperset(conjunto3B)
print(resultado2)

# 2º Con operadores de comparación:

resultado2B = conjunto3 > conjunto3B
print(resultado2B)

print("-----------------------------")


# 4 - ISDISJOINT: Verificar si hay algún número en común. Si hay alguna coincidencia nos dará Falso.

print("Verificar si hay algún número en común:")

resultado3 = conjunto3.isdisjoint(conjunto3B)
print(resultado3)











