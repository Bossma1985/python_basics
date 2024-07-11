# Listas: listado de datos. Se pone entre corchetes []

lista = ["Rafa Botella" , "Bossma5" , True , 1.82]

# Imprime la lista entera
#print(lista)

# Imprime el índice de la lista qe seleccionesentre corchetes
#print(lista[1])

# Las listas dejan modificar sus datos
# lista[1] = "maquina"

#print(lista)


# Tupla (son como las listas pero no se pueden modificar los datos individualmente a posteriori, aunque si sepuede ambiar laTupla entera)
# Se pone entre parentesis ()
tupla = ("Rafa Botella" , "Bossma5" , True , 1.85)

# Imprime la tupla entera
#print(tupla)

# Imprime el índice de la tupla que selecciones entre corchetes []
#print(tupla[1])

# Las tuplas NO dejan modificar sus datos, esto da error
#tupla[1] = "maquina" 
#print(tupla)


# Creando un conjunto (set) se agrupa con llaves {} No tienen orden fijo en el índice. 

conjunto = {"Rafa Botella" , "Bossma5" , True , 1.85}

# Se puede redefinir, pero como en las tuplas no se pueden cambiar datos específicos.

conjunto = {"cambio el conjunto entero"}

#print(conjunto)

# No puede haber datos duplicados. En este caso elimina un "Rafa Botella"

conjunto = {"Rafa Botella" , "Bossma5" , True , 1.85 , "Rafa Botella"}

#print(conjunto)


# Creando un diccionario (dict) se abre con las llaves {} y se identa como un javascript.
# En vez de mostrar el valor por el índice lo muestra por el nombre asociado.
# El nombre asociado es el (Key) y el dato es el (value)

diccionario = {
    'nombre' : "Rafa Botella",
    'canal' : "Bossma5",
    '¿Quiere aprender?' : True,
    'edad' : 39,
    'elemento duplicado' : "Rafa Botella"
}
# Se puede pedir el diccionario entero.
print(diccionario)

# Se puede pedir un dato concreto usando su nombre asociado. 
print(diccionario['canal'])


# Saber tipo de dato: Se puede poner cualquier dato.

tipo_de_dato = type (diccionario)
print(tipo_de_dato)