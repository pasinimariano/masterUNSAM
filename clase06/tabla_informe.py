# Ejercicio 3.13: Recolectar datos
# tabla_informe.py

import csv
import numpy as np


def carga_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con los datos del archivo.
    La funcion recibe como parametro un archivo .csv
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    carga = []

    for n_row, row in enumerate(rows, start=1):
        try:
            record = dict(zip(headers, row))
            carga.append(record)
        except IndexError:
            print(f'Fila {n_row} en el archivo {nombre_archivo}: No pude interpretar: {row}')

    return carga


def leer_precios(nombre_archivo):
    """
    Devuelve una lista de diccionarios con los datos del archivo,
    recibe como parametro un archivo .csv
    """

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    stock = []

    for n_row, row in enumerate(rows, start = 1):
        try:
            producto = dict(nombre=row[0], precio=row[1])
            stock.append(producto)
        except IndexError:
            print(f'Fila {n_row} en el archivo {nombre_archivo}: No pude interpretar: {row}')

    return stock


def hacer_informe(data1, data2):

    """
    Devolvera una lista de diccionarios unificando los dos archivos
    y generara una diferencia entre los precios de ambos (ganancia o perdida).
    Mostrara por consola estos datos en forma de tabla ordenada.
    """

    informe = np.array([dict(nombre=str(x['nombre']),
                             cajones=int(x['cajones']),
                             precio=float(x['precio']),
                             diferencia=float(y['precio']) - float(x['precio']))
                        for x in data1 for y in data2
                        if x['nombre'] == y['nombre']])

    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('-' * 10 + ' ') * len(headers)
    valores = [tuple(i.values()) for i in informe]
    print('%10s %10s %10s %10s' % headers)
    print(sep)
    [print('%10s %10d %10.2f %10.2f' % valor) for valor in valores]

    return informe
    

def imprimir_informe():
    """
    Recibirá las 3 funciones
    """

    camion = carga_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    informe = hacer_informe(camion, precios)

    return informe


imprimir_informe()
