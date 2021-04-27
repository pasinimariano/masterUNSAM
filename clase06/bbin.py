# Ejercicio 6.14: Búsqueda binaria
# bbin.py

def donde_insertar(lista, x):

    lista_ordenada = sorted(lista)
    pos = 0
    izq = 0
    der = len(lista_ordenada) - 1

    while izq <= der:
        medio = (izq + der) // 2
        if lista_ordenada[medio] == x:
            pos = medio
        if lista_ordenada[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1

    if izq > der and lista_ordenada[pos] != x:
        pos = izq
        print(f'El elemento {x} podria insertarse en la posicion {pos}, en la lista {lista}')
    else:
        print(f'El elemento {x} se encuentra en la posicion {pos}, en la lista {lista}')

    return pos


(donde_insertar([0,2,4,6], 3))
(donde_insertar([0,2,4,6], 4))

