# Ejercicio 3.21: Alturas de una especie en una lista
# obtener_altura.py

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
                'altura_tot' : int(registro['altura_tot']),
                'nombre_com' : str(registro['nombre_com']),
                'espacio_ve' : str(registro['espacio_ve']),
            } 
        
        except Exception as error:
            print('-------------------------------------------------------------------------')
            print(f'Fila {n_cadenas} en el archivo {nombre_archivo}: No pude interpretar: {cadena}')
            print('Error: ', error)
            print('-------------------------------------------------------------------------')
        
        if informe['espacio_ve'] == parque:
            arboles.append({informe['nombre_com'] : informe['altura_tot']})        
    return arboles


def obtener_altura(lista_arboles, especie):

    ''' Devolverá una lista de todas las alturas de los arboles por especie. La especie se especificará como parametro. '''

    informe = lista_arboles
    alturas = []
    for x in informe:
        for k, v in x.items():
            if k == especie:
                alturas.append(float(v))
    
    return alturas


parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
arboles1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
arboles2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[1])
arboles3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[2])

especie = ['Jacarandá']

informe1 = obtener_altura(arboles1, especie[0])
informe2 = obtener_altura(arboles2, especie[0])
informe3 = obtener_altura(arboles3, especie[0])

prom1 = round(sum(informe1) / len(informe1), 2)
prom2 = round(sum(informe2) / len(informe2), 2)
prom3 = round(sum(informe3) / len(informe3), 2)

print('-------------------------------------------------------------------------')
print('El {0} más alto en {1} mide: '.format(especie[0], parques[0]), max(informe1), 'mts')
print('El promedio de altura del {0} en {1} es de: '.format(especie[0], parques[0]), prom1, 'mts')
print('-------------------------------------------------------------------------')
print('El {0} más alto en {1} mide: '.format(especie[0], parques[1]), max(informe2), 'mts')
print('El promedio de altura del {0} en {1} es de: '.format(especie[0], parques[1]), prom2, 'mts')
print('-------------------------------------------------------------------------')
print('El {0} más alto en {1} mide: '.format(especie[0], parques[2]), max(informe3), 'mts')
print('El promedio de altura del {0} en {1} es de: '.format(especie[0], parques[2]), prom3, 'mts')
