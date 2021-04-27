# Ejercicio 2.17: Diccionarios como contenedores
# diccionarios_contenedores.py
# encoding: UTF-8

import csv
from pprint import pprint


def leer_precios(nombre_archivo):

    '''Devuelve una lista de precios, recibe como parametro un archivo .csv'''


    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    stock = []

    try :
        for row in rows:
            precios = dict (nombre = row[0],
                            precio = row[1])
            stock.append(precios)
    except Exception as error:
        print('-------------------------------------------------------------------------')
        print('Surgio un error al cargar los datos, verifiquelos y vuelva a intentar.\n'
            'Error: ', error.args)
        print('-------------------------------------------------------------------------')
    
    return stock

stock = leer_precios('Data/precios.csv')



 
