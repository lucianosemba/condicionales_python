# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

palabra_1 = str(input('Ingrese la primera palabra:'))
palabra_2 = str(input('Ingrese la segunda palabra:'))
palabra_3 = str(input('Ingrese la tercera palabra:'))

orden_palabra = int(input('Como quiere ordenar las palabras?: \n1. Ordenar por orden alfabético \n2. Ordenar por cantidad de letras\nIngresar 1 o 2:'))

# Ordenado alfabéticamente
if(orden_palabra == 1): 
    if((palabra_1 >= palabra_2) and (palabra_1 >= palabra_3)):
        if(palabra_2 > palabra_3):
            print('El orden alfabético es {}, {} y {}'.format(palabra_1,palabra_2,palabra_3))
        else:
            print('El orden alfabético es {}, {} y {}'.format(palabra_1,palabra_3,palabra_2))
    elif((palabra_2 >= palabra_1) and (palabra_2 >= palabra_3)):
        if(palabra_1 > palabra_3):
            print('El orden alfabético es {}, {} y {}'.format(palabra_2,palabra_1,palabra_3))
        else:
            print('El orden alfabético es {}, {} y {}'.format(palabra_2,palabra_3,palabra_1))
    else:
        if(palabra_1 > palabra_2):
            print('El orden alfabético es {}, {} y {}'.format(palabra_3,palabra_1,palabra_2))
        else:
            print('El orden alfabético es {}, {} y {}'.format(palabra_3,palabra_2,palabra_1))

# Ordenado por cantidad de letras
elif(orden_palabra == 2): 
    if((len(palabra_1) >= len(palabra_2)) and (len(palabra_1) >= len(palabra_3))):
        if(len(palabra_2) > len(palabra_3)):
            print('El orden por cantidad de letras es {}, {} y {}'.format(palabra_1,palabra_2,palabra_3))
        else:
            print('El orden por cantidad de letras es {}, {} y {}'.format(palabra_1,palabra_3,palabra_2))
    elif((len(palabra_2) >= len(palabra_1)) and (len(palabra_2) >= len(palabra_3))):
        if(len(palabra_1) > len(palabra_3)):
            print('El orden alfabético es {}, {} y {}'.format(palabra_2,palabra_1,palabra_3))
        else:
            print('El orden alfabético es {}, {} y {}'.format(palabra_2,palabra_3,palabra_1))
    else:
        if(len(palabra_1) > len(palabra_2)):
            print('El orden alfabético es {}, {} y {}'.format(palabra_3,palabra_1,palabra_2))
        else:
            print('El orden alfabético es {}, {} y {}'.format(palabra_3,palabra_2,palabra_1))