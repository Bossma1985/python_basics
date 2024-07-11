cadena1 = "Hola. soy. Rafa. adios."
cadena2 = "Bienvenido máquina"

resultado = cadena1


# Dir es una función que te da un listado de los métodos que se le pueden asociar a cada tipo de dato. 
# Solo hay que escribir el dato dentro del () interior.

#print(dir(4))
#print(dir("s"))

#resultado = dir(cadena1)
#print(resultado)



# MÉTODOS. Estructura: DATO.MÉTODO() y en ocasiones el parámetro dentro de los paréntesis.



# 1 - Retornan un valor:


# UPPER: Convierte todo a mayúscula

mayusc = cadena1.upper()

# LOWER: Convierte todo a minúscula

minusc = cadena1.lower()

# CAPiTALIZE: Convierte todo a minúscula y después pone la primera en mayúscula

primer_letra_mayusc = cadena1.capitalize()



# 2 - Buscan un valor que le pidamos de dentro de la cadena:

# FIND: Ej: encuentra una cadena dentro de otra cadena. Te dice el índice del primer valor que coincide. 
# Si no encuentra coincidencias arroja -1

busqueda_find = cadena1.find("S")


# IDEX: Buscan un valor que le pidamos de dentro de la cadena: Te dice el índice del primer valor que coincide.
# DIFERENCIA: Si no encuentra una coincidencia nos lanza una excepción: Un ERROR.

busqueda_index = cadena1.index("a")



# 3 - Saber si es numérico o alphanumérico

# ISNUMERIC: Da True si es un número y falso si no lo és.

es_numerico = cadena1.isnumeric()

# ISALPHA: Da True si es un alphanumérico y falso si no lo és. 
# SOLO da True si hay letras de la A a la Z, no puede haber espacios ni caracteres especiales

es_alphanumerico = cadena1.isalpha()



# 4 - Buscan cuantas veces se repite un valor dentro de la cadena o cuenta el número de caracteres:

# COUNT: Contamos las coincidencias de una cadena dentro de otra cadena, 
# devuelve la cantidad de veces que se repite el dato. 
# Si no encuentra coincidencias da 0

contar_coincidencias = cadena1.count("a")


# LEN: Contamos cuantos caracteres tiene una cadena. 
# MUY IMPORTANTE: LEN es una función y se cambia la estructura

contar_caracteres = len(cadena1)



# 5 - Saber si una cadena empieza o termina con unos datos determinados.

# STARTSWITH: Verifica si una cadena comienza con otra cadena, si es así devuelve True.

empieza_con = cadena1.startswith("Ho")

# ENDSWITH: Verifica si una cadena comienza con otra cadena, si es así devuelve True, de lo contrario da False

termina_con = cadena1.endswith("fa")



# 6 - Reemplazar na adena por otra

# REPLACE: cambia la adena dada por la nueva que le indiques

cadena_nueva = cadena1.replace("." , ",")

# SPLIT: Separar cadenas con la cadena que le damos. Separa según el valor que le demos: , . saltos de linea ...

separar_cadena = cadena1.split(",")






print(separar_cadena)