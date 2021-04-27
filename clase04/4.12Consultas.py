# Ejercicio 4.12: Consultas de datos
# 4.12Consultas.py

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
myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]

print(myn)

myn2 = [s for s in camion if s['cajones'] > 100]

print(myn2)

costo10k = [ s for s in camion if s['cajones'] * s['precio'] > 10000 ]

print(costo10k)