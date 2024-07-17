# Creando una lista con LIST

lista = list(["Hola" , True , 38 , "12" , 55 , False])


# Devulve la cantidad de elementos que contiene la lista. 
# Recordar que LEN es una función y por eso cambia la sintaxis.

cantidad_de_elementos = len(lista)




# Agregando elementos a las listas:

# APPEND: Agregando un elemento al final de la lista.

lista.append("agregado con append")


# INSERT: agrega un elemento en un índice específico.

lista.insert(5 , "añado con insert en índice 5")


# EXTEND: Agrega varios elementos a la lista. 
# La sintaxis cambia al poner los corchetes de lista dentro de los paréntesis

lista.extend(["Rafael B" , 57])



# Eliminando elementos de las listas:

# POP: Eliminando un elemento de la lista por su índice:

#lista.pop(2)

# Un truco para eliminar elementos de atrás hacia adelante y viceversa. 
# Elimina solo el índice y no el número de elementos: -1 elimina el último, -2 el antepenúltimo...

lista.pop(-2)

# Y de esta forma lo mismo pero eliminando los elementos por índice desde el principio

lista.pop(0)


# REMOVE: Borrando un elemento de la lista por su valor:
# Solo elimina el elemento si el valor es IDÉNTICO por entero. Si no encuentra da exepción.


lista.remove(38)


# Eliminando todos los elementos de la lista
# CLEAR: Elimina TODOS los elementos

#lista.clear()

#print(lista)




lista2 = [45 , 6 , 90 , True, False]



# SORT: Ordena la lista de menor a mayor. Ordenando las listas. No aplica a strings.

#lista2.sort()

# Para ordenarle del revés se pone "reverse = True" dentro del paréntesis:

#lista2.sort(reverse = True)



# REVERSE: invierte los elementos de la lista según su posición sin importar su valor.


print(lista2)

lista2.reverse() # Aquí invierto la lista sin un orden de "< a >" ó "> a <"
#print(lista2)

#print(type((lista2)))

print(lista2)