# Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
# camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    precios = []

    for row in rows:
        try:
            precio_cajones = float(row[1]) * float(row[2])
            precios.append(precio_cajones)
        except Exception as error:
            print('-------------------------------------------------------------------------')
            print('Surgio un error al cargar los datos, verifiquelos y vuelva a intentar.\n'
                'Error: ', error.args)
            print('-------------------------------------------------------------------------')

    precio_total = sum(precios)
    return precio_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo Total: ', costo)
