# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas.
# busqueda_en_listas.py


def busqueda_lineal_lordenada(lista, e):
    """
    Encargada de buscar un elemento (e) y retornar la posicion en la que se encuentra, y la cantidad de
    veces que este aparece.
    Si el elemento no se encuentra en la lista el programa retornará -1.
    """

    # Se establece -1 por default, en caso de que el elemento no se encuentre
    pos = -1
    # Si el elemento aparece, el contador devolvera la cantidad de veces.
    cont = 0

    for index, element in enumerate(sorted(lista)):
        if element > e:
            break
        elif element == e:
            pos = index
            cont += 1
        else:
            continue

    return pos, cont


def busqueda_binaria(list_, x, verbose=False):
    """
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """
    if verbose:
        print(f'[DEBUG] left |right |middle')
    # Se establece -1 por default, en caso de que el elemento no se encuentre
    pos = -1
    right = len(list_) - 1
    left = 0

    while left <= right:
        middle = (left + right) // 2
        if verbose:
            print(f'[DEBUG] {left:3d} |{right:>3d} |{middle:3d}')
        if list_[middle] == x:
            pos = middle
        if list_[middle] > x:
            right = middle - 1
        else:
            left = middle + 1

    return pos
