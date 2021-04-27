# Ejercicio 4.19: Lista de altos de Jacarandá
# 4.19AltosJacaranda.py

import csv
from pprint import pprint


def leer_arboles(nombre_archivo):

    """ Se encargará de crear una lista, que contendrá todos los datos del archivo. 
    Cada dato estará almacenado en forma de diccionario. """

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)
    data = []

    registros = [ items for items in cadenas ]
    for x in registros:
        data.append(dict(zip(cabeceras, x)))

    return data 


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especie = 'Jacarandá'
jacaranda = [ float(arbol['altura_tot']) 
              for arbol in arboleda 
              if arbol['nombre_com'] == especie ]

print(f'Alturas del {especie} en todo Buenos Aires')
print('-------------------------------------------')
print(jacaranda)