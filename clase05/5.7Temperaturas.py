# Ejercicio 5.7: Guardar temperaturas
# 5.7Temperaturas.py

import random
import numpy as np


def termometroNp(temp):

    """ Generara una lista, con 999 pruebas realizadas por el termometro, en base a la temperatura ingresada """

    # Genera un margen de error, utilizando numpy
    error = np.array([ random.normalvariate(0, 0.2) for x in range(999) ])
    temp = temp
    # Diferencia entre la temperatura real y el margen de error
    dif = np.array([ x + temp for x in error ])

    return dif
    

termometro = termometroNp(37.5)
print(termometro)
np.save('../Data/Temperaturas.npy', termometro)