# Ejercicio 7.10: Caminatas al azar
# randomWalk.py

import numpy as np
import matplotlib.pyplot as plt


def random_walk(largo):
    """
        Generara numeros al azar entre el -1 y el 2, en un largo determinado, y luego los sumara.
            pre: determinar el largo con un numero entero.
            post: devolverá una lista del largo determinado con los numeros generados aleatoriamente
            ya sumados.
    """
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def plotter_walk(n):
    """
        Se encargara de crear un plotter con 3 subplots.
            pre: el largo ingresado en el parametro debe ser un entero.
            post: devolverá una gráfica, con 3 subplots. El primero mostrara 12 trayectorias diferentes.
            El segundo, la trayectoria que mas se aleja del punto de partida.
            Y el tercero, la trayectoria que menos se aleja del punto de partida.
    """
    caminatas = [random_walk(n) for x in range(12)]

    plt.figure(figsize=(12, 8))

    ax = plt.subplot(2, 1, 1,
                     title='12 caminatas al azar',
                     xlabel='Tiempo',
                     ylabel='Distancia al origen')

    for caminata in caminatas:
        ax.plot(caminata)

    plt.yticks([500, 0, -500])
    plt.xticks([])
    # ----------------------------------------
    lejana = []
    cercana = []

    for caminata in caminatas:
        maximo = max(abs(max(x)) for x in caminatas)
        minimo = min(abs(min(y)) for y in caminatas)
        if maximo in caminata:
            lejana = caminata
        if minimo in caminata:
            cercana = caminata
        else:
            pass
    # ----------------------------------------
    plt.subplot(2, 2, 3,
                title='La caminata que más se aleja',
                xlabel='Tiempo',
                ylabel='Distancia al origen',
                sharey=ax,
                sharex=ax)

    plt.plot(lejana, color='red')
    # ----------------------------------------
    plt.subplot(2, 2, 4,
                title='La caminata que menos se aleja',
                xlabel='Tiempo',
                ylabel='Distancia al origen',
                sharey=ax)

    plt.plot(cercana, color='green')
    # ----------------------------------------

    plt.show()


plotter_walk(100000)
