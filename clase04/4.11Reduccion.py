# Ejercicio 4.11: Reduccion de secuencias
# 4.11Reduccion.py

import csv

def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion,  recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding= 'utf8')
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
        print('Surgio un error al cargar los datos, en el archivo: ', nombre_archivo, '.\n'
              'Error: ', error.args)
        print('-------------------------------------------------------------------------')

    return lote

camion = carga_camion('../Data/camion.csv')
costo = sum([ s['cajones'] * s['precio'] for s in camion ])

print(costo)

