# Promedio de duración:

otros_cursos_max = 7
otros_cursos_min = 2.5
otros_cursos_promedio = 4
dalto_curso = 1.5


# Duración de crudos:

crudo_promedio = 5
crudo_dalto = 3.5


# Diferencias de duración:

diferencia_min = 100 - dalto_curso / otros_cursos_min * 10
diferencia_max = 100 - dalto_curso *1000 // otros_cursos_max / 100  # Fórmula para que solo entregue 2 decimales en caso que nos de 3 o más. 
                                                                    # Explicado en el minuto 02:55:00 del tutorial de Dalto.
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 10


# Calculando el porcentaje del tiempo vacio borrado:

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


# Mostrando las diferencias de duración:

print("------------------------")

print("El curso de Dalto dura:")


print(f" - Un {diferencia_min}% menos que el más rápido")
print(f" - Un {diferencia_max}% menos que el más lento")
print(f" - Un {diferencia_promedio}% menos que el promedio")


# Mostrando la cantidad de espacios vacios que se borran:

print("------------------------")

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimina un {tiempo_vacio_dalto}% de tiempo vacio")


# Mostrando diferencias si los cursos durara 10 horas.

print("------------------------")

print(f"Ver 10 horas de este curso equivale a ver {1000 * otros_cursos_promedio // dalto_curso / 100} horas de otro curso")
print(f"Ver 10 horas de otros cursos equivale a ver {1000 * dalto_curso // otros_cursos_promedio / 100} horas de este curso")


print("------------------------")

