# Ejercicio 4.14: Extraer datos de una arhcivo CSV
# 4.14ExtraerData.py

import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

select = ['nombre', 'cajones', 'precio']

indices = [ headers.index(ncolumna) for ncolumna in select ]

print(indices)

row = next(rows)

record = {nColumna : row[index] for nColumna, index in zip(select, indices) }

print(record)

camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]

print(camion)