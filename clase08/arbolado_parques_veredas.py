# Ejercicio 8.9: Comparando especies en parques y en veredas
# arbolado_parques_veredas.py
import pandas as pd

from arboladoLineal import lectura_lineal
from boxplot import boxplot_data


def comparar_df(df1, columns1, df2, columns2, names=None, n_column=None, value_column=None):
    """
        pre : Se necesita dos archivos DataFrame para que funcione.
                Especificar los nombres de las columnas que se desean comparar.
                Especificar names, si se desea intercambiar el nombre de las columnas en ambos
                    DataFrames. (debe tener la misma cantidad de columnas)
                Si se desea agregar nuevas columnas, especificar n_column y value_column (ambos
                    con dos posiciones, para cada DataFrame).
        post :  Devolverá una union entre ambos DataFrame.
    """

    df1_ = lectura_lineal(path_file=df1, columnas=columns1).copy()
    df2_ = lectura_lineal(path_file=df2, columnas=columns2).copy()

    if names is not None:
        df1_.columns = names
        df2_.columns = names

    if n_column is not None:
        df1_.insert(3, n_column[0], value_column[0], True)
        df2_.insert(3, n_column[1], value_column[1], True)

    df_comparados = pd.concat([df1_, df2_], ignore_index=True)

    return df_comparados


"""
PRUEBA
df_comp = comparar_df(df1='../Data/arbolado-publico-lineal-2017-2018.csv',
                      columns1=['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol'],
                      df2='../Data/arbolado-en-espacios-verdes.csv',
                      columns2=['nombre_cie', 'diametro', 'altura_tot'],
                      names=['nombre_especie', 'diametro', 'altura'],
                      n_column=['ambiente', 'ambiente'],
                      value_column=['vereda', 'parque'])

boxplot_data(file=df_comp,
             column='ambiente',
             grupo='diametro',
             data=['vereda', 'parque'])

boxplot_data(file=df_comp,
             column='ambiente',
             grupo='altura',
             data=['vereda', 'parque'])
"""


