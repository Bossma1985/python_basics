

diccionario = {
    "Nombre" : "Rafa",
    "Apellido" : "Botella",
    "Edad" : 39,
    "Localidad" : "Simat"
}

print(type(diccionario))

# Para que nos muestre la clave. Recordar que la variable "key" puede ser cualquier nombre, solo es orientativa.

for key in diccionario:
    print(key)
    
# Para acceder a la clave y el valor debemos añadir el método ITEMS()

for key in diccionario.items():
    print(key)
    
    
# Ejemplo con variables y f-string. key y value son variables con nombres elegidos al azar.

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")