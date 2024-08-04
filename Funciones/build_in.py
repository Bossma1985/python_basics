

# 1 - MAX: encontrando el valor máximo detro listas, tuplas, conjuntos

lista = [2, -5, 18, 12, 1, 33]

numero_mas_alto = max(lista)
print(numero_mas_alto)



# 2 - MIN: encontrando el valor mínimo detro de detro listas, tuplas, conjuntos

numero_mas_bajo = min(lista)
print(numero_mas_bajo)


print(f"El número más alto es: {numero_mas_alto} y el número más bajo es: {numero_mas_bajo}")

print("------------------------------")


# 3 - ROUND: Redondea el número y también sirve para elegir el número de decimales sin estar creando fórmulas:

# Forma NO optima de redondear y dejar 2 decimales:

print("Determinar decimales de forma NO óptima")

numero = round(12.468905*100)   # Con la función ROUND eliminamos los decimales y nos quedamos solo con el 12 para multiplicarlo * 100 y obtener el 1247.
print(numero/100)                   # Aquí lo / 100 para correr la coma dos lugares a la izquierda y obtenemos 12,47

# Forma óptima de hacerlo con la función ROUND. El resultado es el mismo con menos código. 
# El valor detrás de la coma determina el número de decimales.

print("Determinar decimales de forma óptima")

numero2 = round(25.248965,2)
print(numero2)

print("------------------------------")
 
# 4 - BOOL: Retorna False -> 0 , vacío, False, None / Retorna True -> Distinto a 0, True, cadena, datos no vacíos.

print("probando con BOOL para que de False:")

bool1 = bool()
bool2 = bool(0)
bool3 = bool(False)
bool4 = bool(None)
bool9 = bool([])



print(bool1)
print(bool2)
print(bool3)
print(bool4)
print(bool9)

print("probando con BOOL para que de True:")

bool5 = bool("gfdhñlj")
bool6 = bool(7)
bool7 = bool(True)
bool8 = bool(["fff", 5, True])


print(bool5)
print(bool6)
print(bool7)
print(bool8)


# 5 - ALL: Retorna True si TODOS los valores son verdaderos.

print("probando con la función ALL para que de True:")

all1 = all([3, "eee", True, [56, 7, 9]])

print(all1)

print("probando con la función ALL para que de False:")    # Solo hay que poner un valor False. Ej: 0

all2 = all([0, "eee", True, [56, 7, 9]])

print(all2)


# 6 - SUM: suma todos los valores. Es indispensable que sean números.

print("Suma de números con la función SUM:")

numeros = [30, 5, 10, 10]

sum1 = sum(numeros)

print(sum1)




# SUM, MAX y MIN devuelven excepciones si no dan correcto. ¡¡IMPORTANTE!!





