# Ejercicio 3.9: La función zip()
# informe.py

import csv
from pprint import pprint


def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion en la posicion [0], como así también devuelve 
    el precio total del lote en la posicion [1].
    La funcion recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []
    precios = []

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            cajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total = cajones * precio
            lote.append(record)
            precios.append(costo_total)

        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    
    precio_total = sum(precios)
    return lote, precio_total

lote = carga_camion('../Data/fecha_camion.csv')
print('-------------------------------------------------------------------------')
print('Lote: ')
pprint(lote[0])
print('-------------------------------------------------------------------------')

print('Precio total del lote: $', lote[1])

print('-------------------------------------------------------------------------')