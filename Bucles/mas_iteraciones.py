# Aquí tenemos un bucle normal:

frutas = ["Banana", "Naranja", "Melón", "Pera", "Melocotón", "Papaya", "Ciruelas"]
cadena = "Hola Rafa"
numeros = [2, 6, 8, 13]

for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")

print("-------------------------")
    

# CONTINUE: Aquí un método para saltarse un elemento. En este ejemplo se salta la "Pera" y sigue ejecutándose.

for fruta in frutas:
    if fruta == "Pera":
        continue
    print(f"Me voy a comer una: {fruta}")


print("-------------------------")


# BREAK: Evitar que el bucle siga ejecutándose desde el elemento que le marques

for fruta in frutas:
    if fruta == "Pera":
        break
    print(f"Me voy a comer una: {fruta}")
    

print("-------------------------")



# Iterar una cadena de texto. También cuentan los espacios vacíos.

for letra in cadena:
    print(letra)
    

print("-------------------------")


# Forma NO óptima de modificar valores con FOR: Este ejemplo duplica el valor *2

numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
print(numeros_duplicados)


print("-------------------------")


# Forma óptima de modificar valores con FOR: Este ejemplo duplica el valor *2 en una sola linea de código. 
# Se puede agregar cualquier expresión a la x (x**2, x/88, x+5...) y se añadirá a la variable. Como siempre; x es un nombre aleatorio.

numeros_duplicados2 = [x*2 for x in numeros]
print(numeros_duplicados)


print("-------------------------")