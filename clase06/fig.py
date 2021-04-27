# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:29:15 2021

@author: Micaela
"""
# Ejercicio 5.9
import numpy as np
import random


def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album


album = crear_album(500)
print(album)

# Ejericio 5.10
'''Defino una función que toma el album y si esta incompleto devuelve True'''


def album_incompleto(A):  #
    incompleto = False
    for i in A:
        if i == 0:
            incompleto = True
    return incompleto


album_1 = album_incompleto(album)
print(album_1)

# Ejercicio 5.11

'''Recibe el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) 
y devuelva un número entero aleatorio que representa la figurita que nos tocó'''


def comprar_figu(figus_total):
    figuritas = random.randint(1, figus_total)
    return figuritas


figurita = comprar_figu(10)
print(figurita)


# Ejercicio 5.12

def cuentas_figus(figus_total):
    figuritas_compradas = 0  # Defino contador de figuritas que compro
    album = crear_album(figus_total)  # Creo el album
    print(album)
    while album_incompleto(album):  # Mientras el album este incompleto
        figurita = comprar_figu(figus_total)  # ELige una figurita random
        print(figurita)
        album[
            figurita-1] += 1  # Le sumo 1 a la posicion de la figurita en el album creado.En python es la posicion -1 ya que comienza con 0
        figuritas_compradas += 1  # Sumo 1 al contador definido
    print(figuritas_compradas)
    print(album)
    return figuritas_compradas


album_comple = cuentas_figus(12)
print(album_comple)
