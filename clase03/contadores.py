# Ejercicio 3.11: Contadores
# contadores.py

import csv
from pprint import pprint
from collections import Counter


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

lote = carga_camion('../Data/camion.csv')

tenencias = Counter()
print(lote[0])

for x in lote[0]:
    tenencias[x['nombre']] += int(x['cajones'])

print('-------------------------------------------------------------------------')

print('Tenencias lote 1: ',tenencias)

print('-------------------------------------------------------------------------')

lote2 = carga_camion('../Data/camion2.csv')

tenencias2 = Counter()

for x in lote2[0]:
    tenencias2[x['nombre']] += int(x['cajones'])

print('Tenencias lote 2: ',tenencias2)

print('-------------------------------------------------------------------------')

combinadas = tenencias + tenencias2

print('Tenencias combinadas: ', combinadas)

print('-------------------------------------------------------------------------')