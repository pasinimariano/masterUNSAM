# Ejercicio 3.13: Recolectar datos
# tabla_informe.py

import csv
from pprint import pprint


def carga_camion(nombre_archivo):

    '''Devuelve una lista del lote del camion en la posicion [0], como así también devuelve 
    el precio total del lote en la posicion [1].
    La funcion recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    lote = []
    precios = []

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            cajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total = cajones * precio
            lote.append(record)
            precios.append(costo_total)

        except ValueError:
            print(f'Fila {n_row}: No pude interpretar: {row}')
    
    precio_total = sum(precios)
    return lote

def leer_precios(nombre_archivo):

    '''Devuelve una lista que contendrá un diccionario con los datos del archivo,  
    recibe como parametro un archivo .csv'''

    f = open(nombre_archivo, encoding='utf8')
    rows = csv.reader(f)
    stock = []

    for n_row, row in enumerate(rows, start = 1):
        try :
            records = dict (nombre = row[0],
                            precio = row[1])
            stock.append(records)

        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_row} en el archivo {nombre_archivo}: No pude interpretar: {row}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
    
    return stock

def hacer_informe(data1, data2):

    informe1 = data1
    informe2 = data2
    informe_completo = []

    for x in informe1:
        producto = x['nombre']
        cajones = int(x['cajones'])
        precio_cajon = float(x['precio'])
        for y in informe2:
            producto_local = y['nombre']
            precio_local = float(y['precio'])
            if producto == producto_local:
                diferencia_precio = round(precio_local - precio_cajon, 2)
                data_final = dict(nombre = producto,
                                cajones = cajones,
                                precio = precio_cajon,
                                diferencia = diferencia_precio)
                informe_completo.append(data_final)
    
    return informe_completo
    
camion = carga_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
sep = '---------- ---------- ---------- ----------'

print('%10s %10s %10s %10s' % headers)
print(sep)

for i in informe:
    values = i.values()
    tuple_values = tuple(values)
    print('%10s %10d %10.2f %10.2f' % tuple_values)