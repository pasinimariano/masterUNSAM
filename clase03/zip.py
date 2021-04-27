# Ejercicio 3.9: La función zip()
# zip.py


import csv
from pprint import pprint

def costo_camion(nombre_archivo):

    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    f = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(f)
    headers = next(rows)
    precios = []

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            cajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total = cajones * precio
            precios.append(costo_total)

        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    
    precio_total = sum(precios)
    return precio_total

costo = costo_camion('../Data/camion.csv')
print('camion.csv: $', costo)       

costo = costo_camion('../Data/fecha_camion.csv')
print('fecha_camion.csv: $', costo)
