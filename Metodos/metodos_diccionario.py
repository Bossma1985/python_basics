# DICCIONARIOS:

diccionario = {
    "Nombre" : "Rafa",
    "Edad" : 39,
    "Localidad" : "Simat"
}

# GET: Te devuelve los valores (valeu) de las claves (keys) que pones entre ("ejemplo") 
# Si no encuentra el valor te devuelve "none" y el rograma sigue.

#claves = diccionario.get("Nombre")

#print(claves)


# KEYS: Te devuelve todas las claves (keys) del diccionario: No te da keys por separado. 
# Devuelve un (dict_item)

claves2 = diccionario.keys()

print(claves2)



# POP: Eliminando un elemento del diccionario:

eliminar_elemento = diccionario.pop("Nombre")


print(eliminar_elemento)  # Ya muestra el conjunto sin el (Nombre)


# ITEMS:...


# CLEAR: Elimina todo el diccionario.

claves_borrar = diccionario.clear()


print(claves_borrar)    # Este devuelve "none"
print(diccionario)      # Este VACIA el diccionario 





