# Ejercicio 5.19
# 5.19Figuritas.py

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


def cuantas_figuritas(total_figuritas, paquete_figuritas):
    """ Creara un album, y simulará su llenado (hasta que no queden 0) """
    # Album vacio (0s)
    album_ = crear_album(total_figuritas)
    # Cantidad de figuritas compradas
    historia_figus_pegadas = [0]

    while album_incompleto(album_):
        # Genera una nueva figurita
        paquete = comprar_paquete(total_figuritas, paquete_figuritas)
        # Le suma una figurita mas a la cantidad
        while paquete:
            album_[paquete.pop()] = 1
        figus_pegadas = (album_ > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)        

    # Convierte la lista a un array numpy
    n_paquetes_hasta_llenar= np.array(historia_figus_pegadas)
    prom = (n_paquetes_hasta_llenar <= 850).sum()

    return prom


repeticiones = 1000
cuantas = np.array([ cuantas_figuritas(670, 5) for x in range(repeticiones) ])
lleno = np.array([ x for x in cuantas if x <= 850 ])
promedio = len(lleno) / repeticiones
print('La posibilidad de llenar el album con 850 paquetes o menos es: ',promedio)

