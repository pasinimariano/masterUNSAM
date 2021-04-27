# Ejercicio 2.15: Lista de tuplas
# informe.py

import csv

def costo_camion(nombre_archivo):

    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    precios = []

    for row in rows:
        precio_cajones = float(row[1]) * float(row[2])
        precios.append(precio_cajones)
    
    precio_total = sum(precios)
    return precio_total

def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion'''

    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    carga = []

    for row in rows:
        lote = (row[0], int(row[1]), float(row[2]))
        carga.append(lote)

    return carga

lote = carga_camion('Data/camion.csv')
print('El lote del camion es:\n',lote)

costo = costo_camion('Data/camion.csv')
print('Costo Total: ', costo)

 
