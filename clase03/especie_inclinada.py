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
            arboles.append({'nombre' : informe['nombre_com'],
                            'inclinacion' : informe['inclinacion']})     

    return arboles


def obtener_inclinaciones(lista_arboles):

    ''' Devolverá el arbol más inclinado que existe en el parque seleccionado '''

    informe = lista_arboles
    inclinaciones = [x['inclinacion'] for x in informe]
    max_inclinacion = max(inclinaciones)
    arbol = []

    for x in informe:
        if max_inclinacion == x['inclinacion']:
            arbol.append(x)

    return arbol

parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
arbol1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
arbol2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[1])
arbol3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[2])

informe1 = obtener_inclinaciones(arbol1)
informe2 = obtener_inclinaciones(arbol2)
informe3 = obtener_inclinaciones(arbol3)


print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol mas inclinado es: '.format(parques[0]))
print(informe1)
print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol mas inclinado es: '.format(parques[1]))
print(informe2)
print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol mas inclinado es: '.format(parques[2]))
print(informe3)
