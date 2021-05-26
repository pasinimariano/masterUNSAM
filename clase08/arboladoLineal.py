# Ejercicio 8.7: Lectura y selección
# arboladoLineal.py

import pandas as pd
import os


def lectura_lineal(path_file, columnas=None):
    """
        pre : Se necesita ingresar un path a un directorio.csv válido. Si se desea se pueden colocar
            los nombres de las columas que se desean mostrar. Caso contrario devolverá todas las columnas del
            directorio.
        post : Leerá y devolverá la data ordenada, de un archivo csv.
    """
    file = os.path.join(path_file)
    df = pd.read_csv(file, low_memory=False)

    if columnas is not None:
        try:
            return df[columnas]
        except Exception as e:
            print(e)

    else:
        return df


def ocurrencia_dato(file, dato):
    """
        pre : Se necesita un archivo DataFrame para que funcione. Y especificar el dato
            por el cual se quieren agrupar.
        post : devolverá los 10 datos que más se repiten en el archivo. Con sus
            respectivas cantidades.
    """
    df = file

    most_repeated = df.groupby(dato).size().sort_values(ascending=False).reset_index()
    most_repeated.columns = [dato, 'repeticiones']

    return most_repeated.head(10)


"""
PRUEBA
read_csv = lectura_lineal(path_file='../Data/arbolado-publico-lineal-2017-2018.csv',
                          columnas=['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol'])

print(ocurrencia_dato(file=read_csv, dato='nombre_cientifico'))
"""
