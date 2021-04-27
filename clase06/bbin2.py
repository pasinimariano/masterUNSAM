# Ejercicio 6.15: Insertar un elemento en una lista
# bbin2.py


def ordenar_lista(lista):
    """
    Ordenara la lista.
    """
    return sorted(lista)


def donde_insertar(lista, x, ordenar=False):
    """
    Se encargara de buscar el elemento x (pasado como parametro), en la lista seleccionada.
    Si el elemento se encuentra, se devolvera la posicion del elemento dentro de la lista.
    Caso contrario, se devolvera la posicion en donde se podria agregar el elemento.
    Como tercer parametro, se podrá especificar el parametro ordenar, el cual al pasarle
    True ordenará la lista. (eludir este paso si su lista esta correctamente ordenada).
    """

    if ordenar:
        lista_ = ordenar_lista(lista)
    else:
        lista_ = lista

    # Posicion inicial, la cual sera intercambiada por el recorrido de la lista
    pos = 0
    # Por default diremos que el elemento no se encuentra en la lista
    encontrado = False

    # Punteros de la lista
    inicio = 0
    final = len(lista_) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if lista_[medio] == x:
            pos = medio
            break
        elif lista_[medio] > x:
            final = medio - 1
        else:
            inicio = medio + 1

    if inicio > final and lista_[pos] != x:
        pos = inicio
        print(f'El elemento {x} podria insertarse en la posicion {pos}, en la lista: {lista_}')
    else:
        encontrado = True
        print(f'El elemento {x} se encuentra en la posicion {pos}, en la lista: {lista_}')

    return lista_, pos, encontrado


def insertar(lista, x):
    """
    Si el elemento no se encuentra en la lista, lo agregara en la posicion designada por el orden.
    Caso contrario devolvera la posicion del elemento dentro de la lista.
    """
    elemento = donde_insertar(lista, x)
    lista_ = elemento[0]
    pos = elemento[1]
    encontrado = elemento[2]

    if encontrado:
        return lista_
    else:
        lista_.insert(pos, x)
        print(f'Se agrego el elemento {x} en la lista, en la posicion {pos}')
        return lista_
