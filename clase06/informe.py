# Ejercicio 2.15: Lista de tuplas
# informe.py

import csv

def carga_camion(nombre_archivo):

    ''' Devuelve una lista de diccionarios con los datos del archivo.
    La funcion recibe como parametro un archivo .csv '''

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    carga = []

    for n_row, row in enumerate (rows, start= 1):
        try:
            record = dict(zip(headers, row))
            carga.append(record)
        except Exception as error:
            print(f'Fila {n_row} en el archivo {nombre_archivo}: No pude interpretar: {row}')

    return carga


camion = carga_camion('../Data/camion.csv')
print('El lote del camion es:\n',camion)


 
