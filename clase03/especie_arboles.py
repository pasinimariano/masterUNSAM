# Ejercicio 3.19: Determinar las especies en un parque
# especie_arboles.py

import csv
from pprint import pprint


def especies(nombre_archivo): 

    ''' Devolverá una lista ordenada de los nombres de todos los parques ingresados. '''

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)  
    especie = []

    for n_cadenas, cadena in enumerate(cadenas, start=1):
        registro = dict(zip(cabeceras, cadena))

        try:
            informe = {
                'nombre_com' : str(registro['nombre_com'])
            }

        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_cadenas} en el archivo {nombre_archivo}: No pude interpretar: {cadena}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
        
        especie.append(informe['nombre_com'])
    
    especies = list(set(especie))
    
    return sorted(especies)

informe = especies('../Data/arbolado-en-espacios-verdes.csv')
cantidad = len(informe)

print('-------------------------------------------------------------------------')
print('Las especies que se encuentran en Buenos Aires son: ')
pprint(informe)
print('-------------------------------------------------------------------------')
print('La cantidad total de especies de arboles es de: ', cantidad)
print('-------------------------------------------------------------------------')