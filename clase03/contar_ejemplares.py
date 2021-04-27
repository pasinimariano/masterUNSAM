# Ejercicio 3.20: Contar ejemplares por especie
# contar_ejemplares.py

import csv
from pprint import pprint
from collections import Counter


def leer_parque(nombre_archivo, parque):

    ''' Se encargará de crear una lista, que contendrá todos los datos del archivo. Cada dato estará almacenado en forma de diccionario.
    Para funcionar solicitará dos argumentos, el primero: el nombre del archivo, el segundo: el nombre del parque de donde se quiere 
    obtener la informacion.'''

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)
    arboles = []

    for n_cadenas, cadena in enumerate(cadenas, start=1):
        registro = dict(zip(cabeceras, cadena))

        try:
            informe = { 
                'nombre_com' : str(registro['nombre_com']),
                'espacio_ve' : str(registro['espacio_ve']),
            } 
        
        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_cadenas} en el archivo {nombre_archivo}: No pude interpretar: {cadena}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
        
        if informe['espacio_ve'] == parque:
            arboles.append(informe['nombre_com'])

    return arboles

def contar_ejemplares(archivo):

    ''' Devolvera una lista con la cantidad de arboles por especie que hay. '''
    
    informe = archivo
    contar = Counter(informe).most_common(5)
    data = []
    
    for key , value in contar:
        registros = {
            key : str(value) + ' arboles'
        }

        data.append(registros)

    return data


parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
arboles1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
arboles2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[1])
arboles3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[2])

informe1 = contar_ejemplares(arboles1)
informe2 = contar_ejemplares(arboles2)
informe3 = contar_ejemplares(arboles3)

print('-------------------------------------------------------------------------')
print('Los arboles mas comunes en {0} son: '.format(parques[0]))
pprint(informe1)
print('-------------------------------------------------------------------------')
print('Los arboles mas comunes en {0} {1} son: '.format(parques[1][-3:],parques[1][:5]))
pprint(informe2)
print('-------------------------------------------------------------------------')
print('Los arboles mas comunes en {0} son: '.format(parques[2]))
pprint(informe3)
print('-------------------------------------------------------------------------')