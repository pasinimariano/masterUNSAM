# Ejercicio 8.6: Ordenar el árbol de archivos
# ordenar_imgs.py

import sys
import os
import shutil
from datetime import datetime


def crear_directorio(directorio, nombre_dir):
    """
        pre : se necesitará ingresar un path válido a un directorio. Y el nombre que se
                desea en el subdirectorio.
        post : creará un nuevo subdirectorio dentro del directorio especificado.
    """
    try:
        os.listdir(directorio)
        os.mkdir(os.path.join(directorio, nombre_dir))
        return print(f'Se creo el subdirectorio {nombre_dir} en el directorio {directorio}')

    except FileNotFoundError:
        print('No se pudo encontrar la ruta especificada, verifiquela y vuelva a intentar')
        return False

    except FileExistsError:
        print(f'El subdirectorio {nombre_dir} ya existe en el directorio {directorio}')
        return False


def procesar_img(directorio):
    """
        pre : Se debe ingresar un path a un directorio válido.
        post : Devolverá todos los nombres de los archivos .png dentro del directorio y subdirectorios.
    """
    try:
        os.listdir(directorio)
        for root, dirs, files in os.walk(directorio):
            for name in files:
                file = os.path.join(root, name)
                if '.png' in name:
                    try:
                        fecha_archivo = ''.join((file[-12:-8], '/', file[-8:-6], '/', file[-6:-4]))
                        fecha_formato = datetime.strptime(fecha_archivo, '%Y/%m/%d')
                        ts_fecha = fecha_formato.timestamp()
                        os.utime(directorio, (ts_fecha, ts_fecha))

                        return True

                    except ValueError:
                        print('Los archivos del directorio ya fueron modificados.')
                        return False

    except FileNotFoundError:
        print('No se pudo encontrar la ruta especificada, verifiquela y vuelva a intentar')
        return False


def mover_img(origen, destino):
    """
        pre : Se debe ingresar un path a un directorio válido. Tanto como para el origen, como para el destino.
        post : Moverá los archivos .png al directorio destino, y les modificará el nombre.
    """
    try:
        os.listdir(origen)
        try:
            os.listdir(destino)
            for root, dirs, files in os.walk(origen):
                for name in files:
                    if '.png' in name:
                        origen_ = os.path.join(root, name)
                        destino_ = destino + name[:-11] + '.png'
                        shutil.move(origen_, destino_)

            return True

        except FileNotFoundError:
            print('No se pudo encontrar la ruta especificada en destino, verifiquela y vuelva a intentar')
            return False
    except FileNotFoundError:
        print('No se pudo encontrar la ruta especificada en origen, verifiquela y vuelva a intentar')
        return False


def directorio_vacio(directorio):
    """
        pre : Se debe ingresar un path a un directorio válido.
        post : Recorrerá el directorio y buscará carpetas y subcarpetas vacías, si lo están, estas serán eliminadas.
    """
    try:
        os.listdir(directorio)
        for root, dirs, files in os.walk(directorio):
            if not os.listdir(root):
                os.rmdir(root)
                print(f'Se elimino el directorio {root}, ya que estaba vacío')
                return True
    except FileNotFoundError:
        print('No se pudo encontrar la ruta especificada, verifiquela y vuelva a intentar')
        return False


def main(directorio, procesar, origen, destino, nombre_dir=None):
    """
        Encargada de hacer funcionar el resto de las funciones.
        pre : Se debe ingresar un path a un directorio válido. Tanto en el parametro origen, como en el destino.
            Si se desea crear un subdirectorio se debe especificar el parametro nombre_dir.
    """
    if nombre_dir:
        crear_directorio(directorio, nombre_dir)

    procesar_img(procesar)
    mover_img(origen, destino)
    directorio_vacio(origen)

    return True


if __name__ == '__main__':
    rutas_directorio = sys.argv[1:]
    main(rutas_directorio[0], rutas_directorio[1], rutas_directorio[2], rutas_directorio[3], rutas_directorio[4])
