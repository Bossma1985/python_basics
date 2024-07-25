# 1 - Crear diccionario con founción DICT: 
# La única forma de crear diccionarios vacíos es con la función.

diccionario = dict(nombre="Rafa", apellido="Botella")

print(type(diccionario))
print(diccionario)


# 2 - Crear un diccionario con {}

diccionario2 = {
    "Nombre" : "Rafa",
    "Apellido" : "Botella",
    "Edad" : 39
}

print(diccionario2)


# Las Tuplas pueden ser KEYs porque son inmutables:

diccionario_tupla = {("Titulo","Argumento"):"trarara"}

print(type(diccionario_tupla))
print(diccionario_tupla)


# Las listas no pueden ser KEYs porque son mutables. Esto lanza un error.


#diccionario_lista = {["Titulo2","argumento2"]:"trarara2"}

#print(type(diccionario_lista))
#print(diccionario_lista)


# 3 - Creando diccionarios con FROMKEYS: Es necesario crearlo desde la función DICT: 
# De este modo nos da los datos como si cada carácter del primer STR fuera el KEY. 
# El primer dato es iterable.


diccionario_fromkeys = dict.fromkeys("Nombre","apellido")
print(diccionario_fromkeys)


# Si queremos que se comporte como un diccionario y nos de los valores en None se ha que crear una lista dentro []

diccionario_fromkeys2 = dict.fromkeys(["Nombre","apellido","Domicilio"])
print(diccionario_fromkeys2)