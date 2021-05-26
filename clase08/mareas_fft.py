# mareas_fft.py

import pandas as pd
import matplotlib.pyplot as plt


def lectura_csv(path_file, index=None):
    """
        pre : Se necesita un path válido a un directorio.
                Se puede especificar el indice del archivo.
        post : devolverá la lectura del archivo.
    """
    if index is not None:
        return pd.read_csv(path_file, index_col=[index], parse_dates=True)
    else:
        return pd.read_csv(path_file)


def desplazar(file, desplazamiento, column=None):
    """
        Desplazará las columnas para que sean mas legibles.
    """
    if column is not None:
        df_copy = file[column:].copy()
    else:
        df_copy = file.copy()

    delta_t = 2
    delta_h = 3

    pd.DataFrame([df_copy[desplazamiento[0]].shift(delta_t) - delta_h, df_copy[desplazamiento[1]]]).T.plot()


def main(file_, index_, rango, desplazamiento_):
    """
        Función principal
    """
    df_lineal = lectura_csv(path_file=file_, index=index_)

    desplazar(file=df_lineal, desplazamiento=desplazamiento_, column=rango)

    plt.show()


"""
PRUEBA
main(file_='../Data/mareas.csv',
     index_='Time',
     rango='12-25-2014',
     desplazamiento_=['H_SF', 'H_BA'])
"""
