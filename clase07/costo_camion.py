# Ejercicio 7.2: Función main()
# costo_camion.py

import informe
import sys


def main(argv):
    """
    Computa el precio total del camion
    """
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'path:archivo_camion')
    camion = informe.leer_camion(open(argv[1], encoding='utf8').readlines())
    total = sum([(x['precio']) * (x['cajones']) for x in camion])

    return total


if __name__ == '__main__':
    print('Total costo:', main(sys.argv))
