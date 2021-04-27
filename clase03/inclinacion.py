# Ejercicio 3.22: Inclinaciones por especie de una lista
# inclinacion.py

import csv
from pprint import pprint


def leer_parque(nombre_archivo):

    ''' Se encargará de crear una lista, que contendrá todos los datos del archivo. Cada dato estará almacenado en forma de diccionario.
    Para funcionar solicitará el nombre del archivo como parametro. '''

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
                inclinaciones.append({k[:20] : [v[0], v[1]]})

    return inclinaciones 
                

arboles1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv')

especie = ['Jacarandá']

print('-------------------------------------------------------------------------')
print('La siguiente lista contiene las inclinaciones del {0} ordenadas por cada parque.'.format(especie[0]))
pprint(obtener_inclinaciones(arboles1, especie[0]))