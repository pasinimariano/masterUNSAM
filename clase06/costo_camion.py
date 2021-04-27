# Ejercicio 6.12: Un poco más allá
# costo_camion.py

import informe_funciones as informe


def truck_cost(file_name):
    """
    Computa el precio total del camion (cajones * precio) de un archivo
    """
    truck = informe.leer_camion(file_name)
    total = sum([float(x['precio']) * int(x['cajones']) for x in truck])

    return total




