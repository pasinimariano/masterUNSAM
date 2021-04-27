# Ejercicio 4.18: Lectura de todos los arboles
# 4.18Lectura.py

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


informe = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
pprint(informe)


