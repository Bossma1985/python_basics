variable = "Rafael Botella"

#print(dir(variable))

print(len(variable))    # Te devuelve el número de valores que están dentro de la lista.

print(variable.upper())
print(variable.lower())
print(variable.capitalize())
print(variable.swapcase())

print(variable.replace("Rafa" , "Rafael"))  # Modifica el primer valor por el segundo separado por ,
print(variable.count("a"))  # Cuenta cuantas veces aparece el valor en la lista.

print(variable.startswith("R")) # Confirma si empieza por... Ej: ("R")
print(variable.endswith("e"))   # Confirma si termina por... Ej: ("e")

print(variable.split(" "))  # Corta la cadena según el valor que le pongas () ya sean espacios, letras, comas, saltos de linea...
print(variable.find("a"))   # Encuentra el índice de la primera coincidncia. Si no lo encuentra da: -1
print(variable.index("a"))  # Encuentra el índice de la primera coincidncia. Si no lo encuentra da: Excepción y se bloquea el programa

print(variable.isnumeric()) # Para que de True TODOS deben ser números sin espacios ni caracteres especiales.
print(variable.isalpha())   # Para que de True TODOS deben ser letras sin espacios ni caracteres especiales.

print(variable[0])  # Devuelve el valor del índice que le marcas entre []
print(variable[1])
print(variable[2])
print(variable[-3]) # Si el valor es negativo empieza a contar por el final.
print(variable[-1])


# f-string

nombre = "Rafael"
edad = 39
localidad = "Simat de la Valldigna"

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {localidad}")