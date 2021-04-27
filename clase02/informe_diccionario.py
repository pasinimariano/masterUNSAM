# Ejercicio 2.16: Lista de diccionarios
# informe_diccionario.py
# encoding: UTF-8

import csv
from pprint import pprint


def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion,  recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []

    try:
        for row in rows:
            carga = dict (nombre = row[0],
                          cajones = int(row[1]),
                          precio = float(row[2]))
            lote.append(carga)
    except Exception as error:
        print('-------------------------------------------------------------------------')
        print('Surgio un error al cargar los datos, verifiquelos y vuelva a intentar.\n'
              'Error: ', error.args)
        print('-------------------------------------------------------------------------')

    return lote

lote = carga_camion('Data/camion.csv')
pprint(lote)

total = 0.0
for x in lote:
    total += x['cajones'] * x['precio']

print('Precio total: ', total)


 
