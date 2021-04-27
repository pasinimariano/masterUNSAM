# Ejercicio 6.4: Estructurar un programa como una colección de funciones
# informe_funciones.py

import csv
import numpy as np


def leer_camion(file_name):
    """
    Devuelve una lista de diccionarios con los datos del archivo.
    La funcion recibe como parametro un archivo .csv
    """
    with open(file_name, encoding='utf8') as file_:
        rows = csv.reader(file_)
        headers = next(rows)
        lote = []

        for n_row, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                lote.append(record)
            except IndexError:
                print(f'Fila {n_row} en el archivo {file_name}: No pude interpretar: {row}')

    return lote


def leer_precios(file_name):
    """
       Devuelve una lista de diccionarios con los datos del archivo.
       La funcion recibe como parametro un archivo .csv
       """
    with open(file_name, encoding='utf8') as file_:
        rows = csv.reader(file_)
        stock = []

        for n_row, row in enumerate(rows, start=1):
            try:
                record = dict(nombre=row[0], precio=row[1])
                stock.append(record)
            except IndexError:
                print(f'Fila {n_row} en el archivo {file_name}: No pude interpretar: {row}')

    return stock


def obtener_informe(file1, file2):
    """
    Devolvera una lista de diccionarios unificando dos archivos
    y generara una diferencia entre los precios de ambos (ganancia o perdida).
    """
    informe = np.array([dict(nombre=str(x['nombre']),
                             cajones=int(x['cajones']),
                             precio=float(x['precio']),
                             diferencia=float(y['precio']) - float(x['precio']))
                        for x in file1 for y in file2
                        if x['nombre'] == y['nombre']])

    return informe


def formato_informe(informe):
    """
    Encargada de dar formato a los datos.
    """
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep = ('-' * 10 + ' ') * len(headers)
    valores = [tuple(i.values()) for i in informe]
    print('%10s %10s %10s %10s' % headers)
    print(sep)

    return [print('%10s %10d %10.2f %10.2f' % valor) for valor in valores]


def imprimir_informe():
    """
    Se encargara de parsear los datos de los archivos (utilizando la funcion importada parse_csv()),
    para luego pasarselos como parametro a la funcion hacer_informe().
    Por ultimo se le dara formato al resultado obtenido.
    """

    camion = leer_camion(file_name='../Data/camion.csv')
    precios = leer_precios(file_name='../Data/precios.csv')
    informe = obtener_informe(camion, precios)
    formato = formato_informe(informe)

    return formato




