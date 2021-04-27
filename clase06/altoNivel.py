# Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.
# altoNivel.py

import csv
import numpy as np


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    """
    Devuelve una lista de diccionarios con los datos del archivo.
    La funcion recibe como parametro un archivo .csv
    """

    camion = open(nombre_archivo_camion, encoding='utf8')
    rows = csv.reader(camion)
    headers = next(rows)
    carga = []

    for n_row, row in enumerate(rows, start=1):
        try:
            record = dict(zip(headers, row))
            carga.append(record)
        except IndexError:
            print(f'Fila {n_row} en el archivo {nombre_archivo_camion}: No pude interpretar: {row}')

    precios = open(nombre_archivo_precios, encoding='utf8')
    rows_precios = csv.reader(precios)
    stock = []

    for n_row, row in enumerate(rows_precios, start=1):
        try:
            producto = dict(nombre=row[0], precio=row[1])
            stock.append(producto)
        except IndexError:
            print(f'Fila {n_row} en el archivo {nombre_archivo_precios}: No pude interpretar: {row}')

    informe = np.array([dict(nombre=str(x['nombre']),
                             cajones=int(x['cajones']),
                             precio=float(x['precio']),
                             diferencia=float(y['precio']) - float(x['precio']))
                        for x in carga for y in stock
                        if x['nombre'] == y['nombre']])
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('-' * 10 + ' ') * len(headers)
    valores = [tuple(i.values()) for i in informe]

    print('%10s %10s %10s %10s' % headers)
    print(sep)
    [print('%10s %10d %10.2f %10.2f' % valor) for valor in valores]

    return informe


informe_camion('../Data/camion.csv', '../Data/precios.csv')
