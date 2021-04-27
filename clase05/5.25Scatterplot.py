# Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás
# 5.25Scatterplot.py


import csv
import numpy as np
import matplotlib.pyplot as plt


def leer_arboles(nombre_archivo):

    """ Se encargará de crear una lista, que contendrá todos los datos del archivo. 
    Cada dato estará almacenado en forma de diccionario. """

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)
    
    registros = np.array([ items for items in cadenas ])
    data = np.array([ dict(zip(cabeceras, x)) for x in registros ])

    return data 


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especie = 'Jacarandá'
alturas = np.array([ float(arbol['altura_tot']) 
                        for arbol in arboleda 
                        if arbol['nombre_com'] == especie])
diametros = np.array([ float(arbol['diametro'])
                        for arbol in arboleda 
                        if arbol['nombre_com'] == especie])

plt.scatter(alturas, diametros, s = 25, c = 'green',  alpha = 0.40)
plt.xlabel('Alto (cm)')
plt.ylabel('Diametro (cm)')
plt.title(f'Relación diámetro-altura para {especie}')
plt.show()