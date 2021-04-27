# Ejercicio 3.23: Especie con el ejemplar más inclinado
# mayor_inclinacion.py

import csv
from pprint import pprint


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
                'inclinacion' : int(registro['inclinacio']),
            } 
        
        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_cadenas} en el archivo {nombre_archivo}: No pude interpretar: {cadena}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
        
        if informe['espacio_ve'] == parque:
            arboles.append({informe['espacio_ve'] : [informe['nombre_com'] , informe['inclinacion']]})     

    return arboles


def obtener_inclinaciones(lista_arboles, especie):

    ''' Devolverá una lista de todas las inclinaciones de los arboles por especie. 
    La especie se especificará como parametro. '''

    informe = lista_arboles
    inclinaciones = []
    for x in informe:
        for k, v in x.items():
            if v[0] == especie:
                inclinaciones.append(v[1])

    if len(inclinaciones) != 0:
        inclinaciones = max(inclinaciones)

    return inclinaciones 


parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
arboles1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
arboles2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[1])
arboles3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[2])

especie = ['Falso Guayabo (Guayaba del Brasil)']

informe1 = obtener_inclinaciones(arboles1, especie[0])
informe2 = obtener_inclinaciones(arboles2, especie[0])
informe3 = obtener_inclinaciones(arboles3, especie[0])


print('-------------------------------------------------------------------------')
if isinstance(informe1, int):
    print('El {0} más inclinado en el parque {1}, esta inclinado: '.format(especie[0], parques[0]), informe1, 'grados')
else:
    print('En el parque {0} no hay ningun {1}'.format(especie[0], parques[0]))
print('-------------------------------------------------------------------------')
if isinstance(informe2, int):
    print('El {0} más inclinado en el parque {1}, esta inclinado: '.format(especie[0], parques[1]), informe2, 'grados')
else:
    print('En el parque {0} no hay ningun {1}'.format(especie[0], parques[1]))
print('-------------------------------------------------------------------------')
if isinstance(informe3, int):
    print('El {0} más inclinado en el parque {1}, esta inclinado: '.format(especie[0], parques[2]), informe3, 'grados')
else:
    print('En el parque {0} no hay ningun {1}'.format(especie[0], parques[2]))
