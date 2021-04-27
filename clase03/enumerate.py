# Ejercicio 3.8: Un ejemplo práctico de enumerate()
# enumerate.py

import csv
from pprint import pprint


def costo_camion(nombre_archivo):

    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    f = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []
    precios = []

    for n_row, row in enumerate(rows, start = 1):
        try:
            lote.append(row)
            precio_cajones = float(row[1]) * float(row[2])
            precios.append(precio_cajones)
        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    
    precio_total = sum(precios)
    return precio_total, lote


cost = costo_camion('../Data/missing.csv')
pprint(cost)