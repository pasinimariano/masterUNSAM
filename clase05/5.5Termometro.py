# Ejercicio 5.5: Gaussiana
# 5.5Termometro.py

import random


def termometro(temp):

    """ Generara una lista, con 99 pruebas realizadas por el termometro, en base a la temperatura ingresada """

    # Genera un margen de error
    error = [ random.normalvariate(0, 0.2) for x in range(99) ]
    temp = temp
    # Diferencia entre la temperatura real y el margen de error
    dif = [ x + temp for x in error ]

    return dif
    

def comparacion(lista, prom):

    ''' Se encargará de mostrar el elemento más grande, el más chico, el promedio, y la media
    de una lista de números'''

    # Primer item de la lista
    num_max = lista[0]  
    num_min = lista[0]  
    # Promedio de la lista
    prom = sum(lista) / prom
    # Media de la lista
    media = sorted(lista)[45]

    # Recorrera la lista completa
    for i in range(0, len(lista)):
        # Compara el elemento de la lista con el num_max
        if lista[i] >= num_max:
             # Si el elemento es mayor que el num_max, este último se reemplazará.    
            num_max = lista[i]
        # Compara el elemento de la lista con el num_min    
        if lista[i] <= num_min:   
            # Si el elemento es menor que el num_min, este último se reemplazará. 
            num_min = lista[i]    
        else:
            pass

    data = f'Max: {round(num_max,2)}, Min: {round(num_min,2)}, Prom: {round(prom,2)}, Media: {round(media,2)}'     
    
    return  data


termometro = termometro(37.5)
comparacion = (comparacion(termometro, 99))
print(comparacion)