# Ejercicio 5.1: Generala servida
# 5.1Generala.py

import random


def tirada():

    """ Generará una lista con 5 números aleatorios """

    tirada = [ random.randint(1, 6) for x in range(5) ]

    return tirada


def generala(tirada):

    """ Devolverá True solo si todos los elementos obtenidos en tirada son iguales """

    generala = len(tirada) > 0 and all(elem == tirada[0] for elem in tirada)

    return generala


tiradas = 1000000
dados = [ tirada() for x in range(tiradas) ] 
generala = [ generala(item) for item in dados ]
servida = [ i for i in generala if i ]
promedio = len(servida) / tiradas

print(f'Tire {tiradas} veces, de las cuales {len(servida)} veces saqué generala servida')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {promedio:.6f}.')