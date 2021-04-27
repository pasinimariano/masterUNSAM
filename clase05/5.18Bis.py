# Ejercicios del 5.9 al 5.14: Completando 
# 5.18Bis.py

import matplotlib.pyplot as plt
import numpy as np
import random


def crear_album(total_figuritas):
    """ Utilizando numpy creara un array de 0 (simulando espacios libres para figuritas) """
    album = np.zeros(total_figuritas, dtype = int)

    return album


def album_incompleto(album):
    """ Si encuentra algun 0 (espacio libre) retornará True  """
    if 0 in album:

        return True


def figurita(total_figuritas):
    """ Generara un número aleatorio """
    figurita = random.randint(0, total_figuritas - 1)

    return figurita


def comprar_paquete(total_figuritas, paquete_figuritas):
    """ Generara un paquete de figuritas """
    paquete = [ figurita(total_figuritas) for x in range(paquete_figuritas) ]
    
    return paquete


def calcular_historia_figus_pegadas(total_figuritas, paquete_figuritas):
    album_ = crear_album(total_figuritas)
    historia_figus_pegadas = [0]
    while album_incompleto(album_):
        paquete = comprar_paquete(total_figuritas, paquete_figuritas)
        while paquete:
            album_[paquete.pop()] = 1
        figus_pegadas = (album_ > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas


figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
