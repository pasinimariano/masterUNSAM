# Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
# plot_bbin_vs_bsec.py

import matplotlib.pyplot as plt
import random
import numpy as np


def generar_elemento(rango_max):
    """
    Devuelve un elemento aleatorio
    """
    return random.randint(0, rango_max - 1)


def generar_lista(x, rango_max):
    """
    Devuelve una lista ordenada de x elementos diferentes, entre 0 y rango_max - 1.
    """
    return sorted(random.sample(range(rango_max), k=x))


def busqueda_secuencial(lista_, x):
    """
    Si x se encuentra en la lista, devuelve el indice de su primera aparicion,
    de lo contrario devolvera -1. [0]
    Ademas devuelve la cantidad de comparaciones que realiza la funcion. [1]
    """
    # Se inicializa la cantidad de comparaciones
    comps = 0
    # Posicion por default
    pos = -1
    for index, element in enumerate(lista_):
        comps += 1
        if element == x:
            pos = index
            break

    return pos, comps


def busqueda_binaria(lista_, x):
    """
    Se encargara de buscar el elemento x, en la lista seleccionada.
    Si el elemento se encuentra, se devolvera la posicion del elemento dentro de la lista.
    De no encontrarse en la lista, devolvera False. [0]
    También mostrara la cantidad de comparaciones que se realizaron para recorrer la lista. [1]
    """
    # Se inicializa la cantidad de comparaciones
    comps = 0
    # Posicion por default
    pos = False
    # Punteros de la lista
    inicio = 0
    final = len(lista_) - 1

    while inicio <= final:
        comps += 1
        medio = (inicio + final) // 2
        if lista_[medio] == x:
            pos = medio
            break
        elif lista_[medio] > x:
            final = medio - 1
        else:
            inicio = medio + 1

    return pos, comps


def experimento_secuencial_promedio(lista_, x, rango_max):
    """
    Se encargara de llamar a la funcion generar_elemento(x) en un rango(rango_max)
    para luego utilizar el elemento como argumento en la funcion busqueda_secuencial.
    El resultado sera almacenado en la variable comps_total, y finalmente se computara
    el promedio de comparaciones que se realizaron, el cual sera retornado.
    """
    comps_total = 0
    for item in range(rango_max):
        elemento = generar_elemento(x)
        comps_total += busqueda_secuencial(lista_, elemento)[1]

    comps_prom = comps_total / rango_max

    return comps_prom


def experimento_binario_promedio(lista_, x, rango_max):
    """
    Se encargara de llamar a la funcion generar_elemento(x) en un rango(rango_max)
    para luego utilizar el elemento como argumento en la funcion busqueda_binaria.
    El resultado sera almacenado en la variable comps_total, y finalmente se computara
    el promedio de comparaciones que se realizaron, el cual sera retornado.
    """
    comps_total = 0
    for item in range(rango_max):
        elemento = generar_elemento(x)
        comps_total += busqueda_binaria(lista_, elemento)[1]

    comps_prom = comps_total / rango_max

    return comps_prom


def graficos():
    """
    Encargada de realizar graficos comparativos entre los dos tipos de busqueda.
    """
    m = 10000
    k = 1000
    largos = np.arange(256) + 1
    comps_prom_secuencial = np.zeros(256)
    comps_prom_binario = np.zeros(256)

    for index, elem in enumerate(largos):
        lista_secuencial = generar_lista(elem, m)
        comps_prom_secuencial[index] = experimento_secuencial_promedio(lista_secuencial, m, k)

    for index, elem in enumerate(largos):
        lista_binaria = generar_lista(elem, m)
        comps_prom_binario[index] = experimento_binario_promedio(lista_binaria, m, k)

    plt.plot(largos, comps_prom_secuencial, label='Busqueda secuencial', color='red')
    plt.plot(largos, comps_prom_binario, label='Busqueda binaria')
    plt.xlabel('Largo de la lista')
    plt.ylabel('Cantidad de comparaciones')
    plt.title('Complejidad de la busqueda')
    plt.legend()
    plt.show()


graficos()
