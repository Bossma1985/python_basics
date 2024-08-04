

diccionario = {
    "Nombre" : "Rafa",
    "Apellido" : "Botella",
    "Edad" : 39,
    "Localidad" : "Simat"
}
print("tipo de archivo:")
print(type(diccionario))
print("------------------------------")

# Para que nos muestre la clave. Recordar que la variable "key" puede ser cualquier nombre, solo es orientativa.

print("Mostrar solo losK KEYS:")
for key in diccionario:
    print(key)
    
print("------------------------------")


# Para acceder a la clave y el valor debemos añadir el método ITEMS()

print("Mostrando KEYS y VALUE con el método ITEMS:")
for key in diccionario.items():
    print(key)

print("------------------------------")
    
    
# Ejemplo con variables y f-string. key y value son variables con nombres elegidos al azar.

print("Crear cadena f-string añadiendo variables:")
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: '{key}' y el valor es: '{value}'")