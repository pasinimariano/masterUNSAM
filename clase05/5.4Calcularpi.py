# Ejercicio 5.4: Calcular pi
# 5.4CalcularPi.py

import random


def puntos(): 

    """ Generara dos pùntos de manera aleatoria, y realiza la suma de estos, elevado a 2 """

    x = random.random()
    y = random.random()
    z = x ** 2 + y ** 2

    return z


def estimar_pi(puntos, cant):

    """ Calcula la aproximacion a pi, dados los puntos que caen dentro del circulo """

    punto = puntos
    # Separa los puntos que caen dentro del circulo
    dentro = [ x for x in punto if x < 1 ]
    # Aproximación a pi
    pi = (4*len(dentro)) / cant

    return pi


pruebas = 100000
genera = [ puntos() for x in range(pruebas) ]
acercamiento = [ estimar_pi(genera, pruebas) ]

print('El valor estimado de pi es: ', acercamiento)