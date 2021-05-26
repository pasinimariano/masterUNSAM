# Ejercicio 8.5: Recorrer el árbol de archivos
# listar_img.py

import os
import sys


def listar_img(directorio):
    """
        pre : Se debe ingresar un path a un directorio válido.
        post : Devolverá todos los nombres de los archivos .png dentro del directorio y subdirectorios.
    """
    lista_png = []

    try:
        os.listdir(directorio)
        for root, dirs, files in os.walk(directorio):
            for name in files:
                if "png" in name:
                    lista_png.append(name)

        if len(lista_png) == 0:
            return print(f'No existe ningún archivo con extensión .png en el directorio --> {directorio}')
        else:
            return print(lista_png)

    except FileNotFoundError:
        print('No se pudo encontrar la ruta especificada, verifiquela y vuelva a intentar')


if __name__ == '__main__':
    ruta_directorio = sys.argv[1]
    listar_img(ruta_directorio)

