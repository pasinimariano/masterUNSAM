# Ejercicio 6.19: Contar comparaciones en la búsqueda binaria
# comparaciones.py

def ordenar_lista(lista):
    """
    Ordenara la lista del elemento menor al mayor.
    Esto se hace ya que el algoritmo necesita una lista ordenada, para su eficiencia.
    """
    return sorted(lista)


def donde_insertar(lista, x, ordenar=False):
    """
    Se encargara de buscar el elemento x (pasado como parametro), en la lista seleccionada.
    Si el elemento se encuentra, se devolvera la posicion del elemento dentro de la lista.
    Caso contrario, se devolvera la posicion en donde se podria agregar el elemento.
    Como tercer parametro, se podrá especificar el parametro ordenar, el cual al pasarle
    True ordenará la lista. (eludir este paso si su lista esta correctamente ordenada).
    Devolvera 4 elementos, [0] Lista [1] Posicion del elemento o posible posicion
    [2] True o False si lo encuentra o no [3] Cantidad de comparaciones realizadas.
    """

    if ordenar:
        lista_ = ordenar_lista(lista)
    else:
        lista_ = lista

    # Posicion inicial, la cual sera intercambiada por el recorrido de la lista
    pos = 0
    # Por default diremos que el elemento no se encuentra en la lista
    encontrado = False
    # Cantidad de comparaciones que se realizan
    comp = 0

    # Punteros de la lista
    inicio = 0
    final = len(lista_) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        comp += 1
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

    return lista_, pos, comp, encontrado

