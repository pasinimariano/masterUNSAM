# Ejercicio 8.3: Fecha de reincorporación
# licencia.py

from datetime import datetime, timedelta


def licencia_paternidad(inicio_licencia, duracion):
    """
        pre: Se debe especificar la fecha de inicio de licencia,en formato str,
                usando '/' para separar fechas --> 'día/mes/año'.
                La duración será un número.
        post : el return será la fecha de reincorporación.
    """
    try:
        licencia = datetime.strptime(inicio_licencia, '%d/%m/%Y')
        reincorporacion = licencia + timedelta(days=duracion)

        return reincorporacion

    except ValueError:
        print('El mes debe ser especificado con números')
