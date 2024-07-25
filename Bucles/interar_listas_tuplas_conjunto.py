# Crear bucle de todos los elementos de la lista. 
# La variable "animal" solo funciona dentro del bucle y puedes elegir cualquier nombre. Ej: animal, bicho, mascota, trarara....

animales = ["Gato", "Perro", "Caballo", "Pato", "Toro"]
numeros = [2, 5, 9, 13, 18]


# 1 - Recorrer la lista de animales

for animal in animales:
    print(animal)
    
print("-----------------------------")
    
    
# Añadiendo variable a STR para crear bucle 

for animal in animales:
    print(f"Ahora la variable animal es: {animal}")
    

print("-----------------------------")


# Recorrer la lista de números haciendo modificaciones:

for numero in numeros:
    resultado = numero*10
    
    print(f"Ahora el resultado es este: {resultado}")

print("-----------------------------")


# 2 - ZIP: Iterar varias listas al mismo tiempo: Se intercalan la una a la otra. 
# El número de listas puede ser n, pero es necesario que coincidan el numero de elementos en todas ellas. 

for animal,numero in zip(animales,numeros):
    print(f"Recorriendo lista 1: {animal}")
    print(f"Recorriendo lista 2: {numero}")

print("-----------------------------")


# Recorrer listas por su índice: 

# 3 - RANGE: Forma NO óptima de recorrer una lista por su índice. No funciona en los conjuntos.

for num in range(len(numeros)):
    print(numeros[num])
    
    
print("-----------------------------")

# 4 - ENUMERATE: Forma óptima de recorrer una lista por su índice, lo muestra dentro de Tuplas:

for num in enumerate(numeros):
    print(num)
    
    
# Se puede acceder individualmente a los índices o elementos. [0] muestra índice [1] muestra elemento.


for num in enumerate(numeros):
    print(num[0])
    
print("-----------------------------")

# Se puede acceder a los 2 valores creando variables y se pueden añadir a un STR

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor es: {valor}")
    

print("-----------------------------")


# 5 - ELSE

for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero} ")
else:
    print("El bucle terminó")
    
    
    
# TODO LO ANTERIOR ES IGUAL PARA TUPLAS, LISTAS Y CONJUNTOS