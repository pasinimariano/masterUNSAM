# Ejercicio 3.18: Lectura de los árboles de un parque
# arboles.py

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
                'long' : float(registro['long']),
                'lat' : float(registro['lat']),
                'id_arbol' : int(registro['id_arbol']),
                'altura_tot' : int(registro['altura_tot']),
                'diametro' : int(registro['diametro']),
                'inclinacion' : int(registro['inclinacio']),
                'id_especie' : int(registro['id_especie']),
                'nombre_com' : str(registro['nombre_com']),
                'nombre_cie' : str(registro['nombre_cie']),
                'tipo_folla' : str(registro['tipo_folla']),
                'espacio_ve' : str(registro['espacio_ve']),
                'ubicacion' : str(registro['ubicacion']),
                'nombre_fam' : str(registro['nombre_fam']),
                'nombre_gen' : str(registro['nombre_gen']),
                'origen' : str(registro['origen']),
                'coord_x' : float(registro['coord_x']),
                'coord_y' : float(registro['coord_y'])
            } 
        
        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_cadenas} en el archivo {nombre_archivo}: No pude interpretar: {cadena}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
        
        if informe['espacio_ve'] == parque:
            arboles.append(informe)

    return arboles

informe = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
cantidad = len(informe)

print('-------------------------------------------------------------------------')
print('Los siguientes arboles pertenecen al parque: ')
pprint(informe)
print('-------------------------------------------------------------------------')
print('La cantidad total de arboles en este parque es de: ', cantidad)
print('-------------------------------------------------------------------------')

def leer_parque(nombre_archivo, parque):

    ''' Se encargará de crear una lista, que contendrá todos los datos del archivo. Cada dato estará almacenado en forma de diccionario.
    Para funcionar solicitará dos argumentos, el primero: el nombre del archivo, el segundo: el nombre del parque del cual se quiere
    obtener la informacion.'''

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)
    data = []

    registros = [ items for items in cadenas if parque in items]
    for x in registros:
        data.append(dict(zip(cabeceras, x)))

    return data 
