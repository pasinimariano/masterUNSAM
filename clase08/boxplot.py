# Ejercicio 8.8: Boxplots
# boxplot.py

import os
import pandas as pd
import matplotlib.pyplot as plt


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


def boxplot_data(file, column, grupo, data=None):
    """
        pre : Se necesita un archivo DataFrame para que funcione. El segundo parametro, es la columna que se desea.
            El parametro grupo es el dato que solicitará el boxplot, para agrupar la data.
            También si se desea se deberá especificar nombres especificos de la columna seleccionada.
        post : devolverá un boxplot de los datos del archivo.
    """
    if data is not None:
        df_lineal = file[file[column].isin(data)]
    else:
        df_lineal = file[file[column]]

    boxplot_ = df_lineal.boxplot(grupo, by=column)
    boxplot_.plot()

    return plt.show()


"""
PRUEBA
read_csv = lectura_lineal(path_file='../Data/arbolado-publico-lineal-2017-2018.csv',
                          columnas=['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol'])

boxplot_data(file=read_csv,
             column='nombre_cientifico',
             grupo='diametro_altura_pecho',
             data=['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu'])
"""