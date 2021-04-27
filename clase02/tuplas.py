# Ejercicio 2.11: Tuplas
# tuplas.py

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    fila = next(rows)
    t = (fila[0] , int(fila[1]), float(fila[2]))
    print('t: ',t)
    cost = t[1] * t[2]
    print('cost: ',cost)
    t = (t[0], 75, t[2])
    print('t, reemplazada: ', t)
    nombre, cajones, precio = t
    print('nombre: ', nombre)
    print('cajones: ', cajones)
    print('precio: ', precio)
    t = (nombre, 2*cajones, precio)
    print('t, empaquetada: ', t)

costo = costo_camion('Data/camion.csv')