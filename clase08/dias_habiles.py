# Ejercicio 8.4: Días hábiles
# dias_habiles.py

from datetime import datetime, timedelta


def dias_habiles(inicio, fin, feriados=None):
    """
    pre : Se debe especificar la fecha de inicio y fin,en formato str,
            usando '/' para separar fechas --> 'día/mes/año'.
            Especificar una lista, con las fechas de feriados. Usando el mismo
            formato de fechas.
    post : Devolverá una lista con los días hábiles dentro del lapso
            especificado entre inicio y fin.
    """
    if feriados is not None:
        feriados_ = [datetime.strptime(x, '%d/%m/%Y') for x in feriados]
    inicio_ = datetime.strptime(inicio, '%d/%m/%Y')
    fin_ = datetime.strptime(fin, '%d/%m/%Y')
    dias = []

    while inicio_ <= fin_:
        if inicio_.weekday() == 5 or inicio_.weekday() == 6:
            pass
        elif inicio_ in feriados_:
            pass
        else:
            dias.append((inicio_.day, inicio_.month, inicio_.year))

        inicio_ += timedelta(days=1)

    return dias
