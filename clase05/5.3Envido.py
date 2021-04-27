# vEjercicio 5.3: Envido
# 5.3Envido.py

import random
from collections import Counter


def mano():

    """ Otorgará 3 cartas aleatorias. """

    # Valores de las cartas (el 8 y 9 no se utilizan en el truco).
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]  
    # Palos de las cartas.
    palos = ['oro', 'copa', 'basto', 'espada']   
    # Generara un valor por cada palo.
    naipes = [(valor, palo) for valor in valores for palo in palos] 
    # .sample selecciona 3 elementos aleatorios únicos. 
    mano = random.sample(naipes, k = 3)

    return mano


def envido(mano):

    """ Comprueba si el envido es posible. """

    # Separa el palo más común en la mano
    palo_mano = Counter(i[1] for i in mano).most_common(1)
    # Comprueba si en la mano existe más de una carta del mismo palo
    envido = []
    for a, b in mano:
        for x, y in palo_mano:
            if b in x and y >1:
                envido.append((a, b))
    # Establece los valores del envido
    valores = []
    if len(envido) > 0:
        for x, y in envido:
            if x <= 7:   
                x = x + 10
                valores.append(x)
            else:
                x = 10
                valores.append(x)
    # Si existe envido suma los nuevos valores
    valores = sorted(valores)
    try:
        valor_envido = valores[-1] + valores[-2]
        return valor_envido
    except IndexError:
        valores = 0
        return valores

    
mano = mano() 
envido = envido(mano)
print('El valor del envido es: ', envido)


