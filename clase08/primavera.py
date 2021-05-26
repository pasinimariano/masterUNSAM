# Ejercicio 8.2: Cuánto falta
# primavera.py

from datetime import datetime


def cuanto_falta():
    """
        Devolverá el número de días que falta para el inicio de la primavera.
    """

    fecha_actual = datetime.now()
    primavera = datetime(year=fecha_actual.year, month=9, day=22, hour=0, minute=0, second=0)

    return fecha_actual - primavera
