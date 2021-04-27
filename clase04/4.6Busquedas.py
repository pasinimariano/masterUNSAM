# Ejercicio 4.6: Búsquedas de un elemento
# 4.6Busquedas.py


def buscar_elemento(lista, e):

    """ Encargada de buscar un elemento (parametro 2) y retornar la posicion en la que se encuentra, y la cantidad de 
    veces que este aparece. Si el elemento no se encuentra en la lista el programa retornará -1. """

    pos = -1 # Se establece -1 en caso de que no se encuentre el elemento.
    cant = 0

    for i , z in enumerate(lista): # Recorre toda la lista.
        if z == e:                 # Si el elemento de la lista es igual al elemento igresado = True
            pos = i                # Si la condicion se cumple, pos tomará el valor de i (es decir la posicion del elemento)
            cant += 1

    info_pos = f'Elemento {e} posicion: {pos}'
    info_cant= f' ,aparece: {cant} veces'

    return info_pos + info_cant


print(buscar_elemento([1,2,3,2,3,4],1))
print(buscar_elemento([1,2,3,2,3,4],2))
print(buscar_elemento([1,2,3,2,3,4],3))
print(buscar_elemento([1,2,3,2,3,4],5))