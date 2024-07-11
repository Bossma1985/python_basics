
# Uso del "Elif" sirve para enlaza Ifs dentro de la misma ejecución hasta encontrar un True o un else.
# Se pueden poner tantos Elif como se desee

Ingreso_mensual = 20019

#if Ingreso_mensual > 10000:
    #print("Estás bien en todo el mundo")
#elif Ingreso_mensual > 2000:
    #print("Estás bien en España")
#elif Ingreso_mensual > 500:
    #print("Eres pobre")
#else:
    #print("Hoy no comes")
    

# Otro ejemplo de uso más complejo: Ifs anidados:

ingreso_mensual = 2020
gasto_mensual = 10

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit")
    elif ingreso_mensual - gasto_mensual > 10000:
        print("Lo estás petando!")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Buenas ganancias")
    else:
        print("Gastas mucho")
        
elif ingreso_mensual > 2000:
    print("Estás bien en España")
elif ingreso_mensual > 500:
    print("Eres pobre")
else:#
    print("Hoy no comes")