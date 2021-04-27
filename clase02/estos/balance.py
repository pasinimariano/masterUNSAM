# Ejercicio 2.18: Balances
# balance.py
# encoding: UTF-8

import csv
from pprint import pprint


def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion,  recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding= 'utf8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []

    try:
        for row in rows:
            carga = dict (nombre = row[0],
                          cajones = int(row[1]),
                          precio = float(row[2]))
            lote.append(carga)

    except Exception as error:
        print('-------------------------------------------------------------------------')
        print('Surgio un error al cargar los datos, en el archivo: ', nombre_archivo, '.\n'
              'Error: ', error.args)
        print('-------------------------------------------------------------------------')

    return lote

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
        print('Surgio un error al cargar los datos, en el archivo: ', nombre_archivo, '.\n'
            'Error: ', error.args)
        print('-------------------------------------------------------------------------')
    
    return stock

def balance_precios():

    lote_camion = carga_camion('Data/camion.csv')
    precios_local = leer_precios('Data/precios.csv')
    data = []

    for x in lote_camion:
        lote_nombre = x['nombre']
        lote_cajones = int(x['cajones'])
        precio_cajones = float(x['precio'] )
        precio_lote = lote_cajones * precio_cajones
        for y in precios_local:
            local_nombre = y['nombre']
            local_precio = float(y['precio'])
            if lote_nombre == local_nombre:
                precio_stock = local_precio * lote_cajones
                data_final = dict(nombre = lote_nombre,
                                  precio_camion = precio_lote,
                                  precio_local = precio_stock)
                data.append(data_final)
    return data

informe= balance_precios()

total_lote = 0.0
total_local = 0.0
diferencia = 0.0

for elem in informe:
    total_lote += elem['precio_camion']
    total_local += elem['precio_local']

diferencia = total_local - total_lote
    
print('Costo total camion: ', round(total_lote, 2))
print('Costo total local: ', round(total_local, 2))
print('Diferencia: ', round(diferencia, 2))
    