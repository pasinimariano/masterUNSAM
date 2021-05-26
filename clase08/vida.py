# Ejercicio 8.1: Segundos vividos
# vida.py

from datetime import datetime, date


def segundos_vida(fecha_nacimiento):
    """
        pre : Se debe especificar tu fecha de nacimiento,en formato str,
                usando '/' para separar fechas --> 'día/mes/año'.
        post : el return de la función es la cantidad de segundos vividos.
    """
    try:
        nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
        actualidad = datetime.now()
        dias_vividos = actualidad - nacimiento

        return dias_vividos.total_seconds()

    except ValueError:
        print('El mes debe ser especificado con números')
