 # Para pedirle un número al usuario:
 
numero = input("Dame un numero ")

# Multiplicando la variable número * 2

resultado = numero * 2

print(resultado)    # El resultado de esto da "22" porque el 2 que devuelve es un "str" 
                    # y al multiplicar str * 2 solo duplica el dato ya que no es numérico.


# LA SOLUCIÓN: Es convertir el dato "str" por un dato tipo número "int" o "float" con la función INT:
# INT lo convierte a entero y FLOAT a decimal

edad = input("Dame tu edad: ")

edad_entero = int(edad)  # Aquí se convierte el "str" en "INT" 
edad_float = float(edad)   # Aquí se convierte el "str" en "FLOAT"

print(f"tu edad es: {edad_entero}")