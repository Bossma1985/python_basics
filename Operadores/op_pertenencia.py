# Operadores de pertenencia: Averiguar si algo está dentro de la variable o no. Es Case Sensitive.

edad1 = 39
nombre1 = "Rafa"
Rafa1 = f"hola soy {nombre1} y tengo {edad1} años"

print("ola" in Rafa1) #True (basta con que coincidan)
print("pedro" in Rafa1) # False
print("Pedro" not in Rafa1) #True
print("hola" not in Rafa1) #False