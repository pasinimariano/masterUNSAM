# Ejercicio 7.5: Arreglemos las funciones existentes
# informe.py

import sys
import numpy as np
from fileParse import parse_interable


def leer_camion(file_name):
    """
        Devuelve una lista de diccionarios con los datos del archivo.
    """
    return parse_interable(file_name, types=[str, int, float])


def leer_precios(file_name):
    """
        Devuelve una lista de diccionarios con los datos del archivo.
    """
    return parse_interable(file_name, has_headers=False, types=[str, float])


def obtener_informe(file1, file2):
    """
        Devolvera una lista de diccionarios unificando dos archivos
        y generara una diferencia entre los precios de ambos (ganancia o perdida).
    """
    return np.array([dict(nombre=str(x['nombre']),
                          cajones=int(x['cajones']),
                          precio=float(x['precio']),
                          diferencia=float(y[1]) - float(x['precio']))
                     for x in file1 for y in file2
                     if x['nombre'] == y[0]])


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


def main(argv):
    """
        Se encargara de parsear los datos de los archivos (utilizando la funcion importada parse_csv()),
        para luego pasarselos como parametro a la funcion obtener_informe().
        Por ultimo se le dara formato al resultado obtenido.
    """
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'path:archivo_camion path:archivo_precios')
    camion = leer_camion(open(argv[1], encoding='utf8').readlines())
    precios = leer_precios(open(argv[2], encoding='utf8').readlines())
    informe = obtener_informe(camion, precios)
    formato = formato_informe(informe)

    return formato


if __name__ == '__main__':
    main(sys.argv)
