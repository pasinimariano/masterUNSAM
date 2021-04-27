# Ejercicios del 5.9 al 5.14: Completando 
# 5.9-5.14Figuritas.py

import numpy as np
import random


def crear_album(total_figuritas):
    """ Utilizando numpy creara un array de 0 (simulando espacios libres para figuritas) """
    return np.zeros(total_figuritas, dtype = int)


def album_incompleto(album):
    """ Si encuentra algun 0 (espacio libre) retornará True  """
    if 0 in album:

        return True


def comprar_figurita(total_figuritas):
    """ Generara un número aleatorio """
    return random.randint(0, total_figuritas - 1)


def cuantas_figuritas(total_figuritas):
    """ Creara un album, y simulará su llenado (hasta que no queden 0) """
    # Album vacio (0s)
    album_ = crear_album(total_figuritas)
    # Cantidad de figuritas compradas
    cantidad = 1

    while album_incompleto(album_):
        # Genera una nueva figurita
        figurita = comprar_figurita(total_figuritas)
        # Le suma una figurita mas a la cantidad
        cantidad += 1
        # Coloca la figurita en su posicion, si esta repetida la sumará
        if album_[figurita] >= 0:
            album_[figurita] += 1

    return cantidad


repeticiones = 1000
cuantas = np.array([ cuantas_figuritas(6) for x in range(repeticiones) ])
promedio = np.mean(cuantas)
print('Promedio de compra para completar album de 6: ', round(promedio), 'figuritas')

repeticiones = 100
cuantas = np.array([ cuantas_figuritas(670) for x in range(repeticiones) ])
promedio = np.mean(cuantas)
print('Promedio de compra para completar album de 670: ', round(promedio), 'figuritas')

np.save('../Data/Figuritas.npy', cuantas)



