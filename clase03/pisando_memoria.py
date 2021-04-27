# Ejercicio 3.5: Pisando memoria
# pisando_memoria.py

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]   
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict({encabezado[0] : fila[0],
                             encabezado[1] : fila[1],
                             encabezado[2] : fila[2]})
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
