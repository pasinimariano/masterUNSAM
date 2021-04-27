# Ejercicio 2.9: Funciones de la biblioteca
# costo_camion_csv.py

import csv
from pprint import pprint

def costo_camion(nombre_archivo):

    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    f = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []
    precios = []

    for row in rows:
        lote.append(row)
        precio_cajones = float(row[1]) * float(row[2])
        precios.append(precio_cajones)
    
    precio_total = sum(precios)
    return precio_total, lote

    f.close()

costo = costo_camion('Data/camion.csv')
print('-------------------------------------------------------------------------')
print('Lote: ')
pprint(costo[1])
print('-------------------------------------------------------------------------')
print('Costo Total del lote: ', costo[0])

