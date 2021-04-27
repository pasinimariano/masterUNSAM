# Ejercicio 6.10: Importar módulos
# imports.py

from fileParse import parse_csv
from pprint import pprint

precios = parse_csv('../Data/precios.csv', types=[str, float])
print('Sin encabezados, y con types')
pprint(precios)
print('-' * 100)

naranja = parse_csv('../Data/precios.csv', select='Naranja', types=[str, float])
print('Sin encabezados, con select, y con types')
print(naranja)
print('-' * 100)

camion = parse_csv('../Data/camion.csv', has_headers=True)
print('Con encabezados')
pprint(camion)
print('-' * 100)

camion_precios = parse_csv('../Data/camion.csv', select=['nombre', 'precio'],
                                     types=[str, float], has_headers=True)
print('Con encabezados, con select y types')
pprint(camion_precios)
