
#Formas de crear Tuplas:

# Con función: Es la única forma de crear Tuplas vacías.

print("1 - Creando tupla con función tuple")

tupla1 = tuple(["casa", "perro", "54",88])

print(type(tupla1))
print(tupla1)

print("------------------------")

# Crear tupla 2 con múltiples datos.

print("2 - Creando tupla con paréntesis")

tupla2 = ("Rojo", "Gato", "avión" , 77)

print(type(tupla2))
print(tupla2)


print("------------------------")

# Crear tupla 2 con 1 solo dato. Solo hay que dejar la coma "," y se puede crear sin paréntesis.

print("3 - Creando tupla con un solo dato")

tupla2B = ("casa", )
tupla2C = "casa", 

print(type(tupla2B))
print(tupla2B)

print(type(tupla2C))
print(tupla2C)
