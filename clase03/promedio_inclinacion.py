# Ejercicio 3.24: Especie más inclinada en promedio
# promedio_inclinacion.py

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

    ''' Devolverá la especie de arbol que mayor promedio de inclinacion posee, y el promedio de inclinacion'''

    informe = lista_arboles

    contar_inclinaciones = Counter()
    for x in informe:
        contar_inclinaciones[x['nombre']] += int(x['inclinacion'])

    nombres = [x['nombre'] for x in informe]
    contar_nombres = dict(Counter(nombres))

    promedios = []

    arbol = []
    
    for key_inclinaciones, value_inclinaciones in contar_inclinaciones.items():
        for key_nombres, value_nombres in contar_nombres.items():
            if key_nombres == key_inclinaciones:
                promedio = round(value_inclinaciones / value_nombres, 2)
                promedios.append({'nombre' : key_nombres,
                                  'promedio' : promedio})  

    inclinaciones = [x['promedio'] for x in promedios]
    max_prom = max(inclinaciones)
    for x in promedios:
        if max_prom == x['promedio']:
            arbol.append(x)

    return arbol


parques = ['LAGO REGATAS', 'CHACABUCO', 'CENTENARIO']
arbol1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[0])
arbol2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[1])
arbol3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parques[2])

informe1 = obtener_inclinaciones(arbol1)
informe2 = obtener_inclinaciones(arbol2)
informe3 = obtener_inclinaciones(arbol3)

print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol con mayor promedio de inclinacion es: '.format(parques[0]))
print(informe1)
print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol con mayor promedio de inclinacion es: '.format(parques[1]))
print(informe2)
print('-------------------------------------------------------------------------')
print('En el parque {0} el arbol con mayor promedio de inclinacion es: '.format(parques[2]))
print(informe3)

