# Ejercicio 6.11: Usemos tu módulo
# moduloFileParse.py

import numpy as np
from fileParse import parse_csv


def hacer_informe(file1, file2):

    """
    Devolvera una lista de diccionarios unificando dos archivos
    y generara una diferencia entre los precios de ambos (ganancia o perdida).
    """
    informe = np.array([dict(nombre=x['nombre'],
                             cajones=x['cajones'],
                             precio=x['precio'],
                             diferencia=y[1] - x['precio'])
                        for x in file1 for y in file2
                        if x['nombre'] == y[0]])

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

    camion = parse_csv('../Data/camion.csv', types=[str, int, float], has_headers=True)
    precios = parse_csv('../Data/precios.csv', types=[str, float])
    informe = hacer_informe(camion, precios)
    formato = formato_informe(informe)

    return formato


imprimir_informe()

