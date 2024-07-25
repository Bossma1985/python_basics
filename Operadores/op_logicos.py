# AND: Solo con que encuentre un False en la cadena arrojará un False, solo da True si TODOS son True. 

resultado1 = True & True    # Da True
resultado2 = False & True   # Da False
resultado3 = True & False   # Da False
resultado4 = False & False  # Da False

# OR: Si una de las 2 condiciones (o las que haya) se cumplen da True, si todas son falsas da False

resultado5 = True | True    # Da True
resultado6 = False | True   # Da True
resultado7 = True | False   # Da True
resultado8 = False | False  # Da False

# NOT: Invierte de False a True y viceversa

resultado9 = not True   # Da False
resultado10 = not False # Da True


print(resultado3)

# EXTRA tabla ASCII: Comprobrar en: https://elcodigoascii.com.ar el valor de cada caracter 
# para ver cual tiene prioridad en un comparativa: 
# En este caso la T = 84 y la C = 67, por tanto nos devolverá True.

ascii_comparativa = "Torete" > "Casa"
print(ascii_comparativa)