# Ejercicio 6.9: Parsear un archivo CSV
# fileParse.py

import csv


def parse_csv(file_name, select=None, types=None, has_headers=False):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un conjunto de columnas, determinando el parametro 'select', 
    -en el caso de que posea encabezados, debe ser una lista de nombes de las columnas a considerar.
    -en el caso que no posea encabezados, se puede filtrar utilizando cualquiera de los datos de la
    lista.(nombres, numeros, fechas, etc)
    Tambien se puede especificar el type de los datos de cada columna, utilizando el 
    parametro 'types', en forma de lista por cada columna.
    Por ultimo si el archivo posee encabezados se debe especificar utilizando el parametro 
    'has_headers = True'. Si no los posee no es necesario pasarle este parametro.
    """
    with open(file_name, encoding='utf-8') as file_:
        rows = csv.reader(file_)

        records = []

        if has_headers:
            # Lee los encabezados
            headers = next(rows)
            # Si se indica un selector de columnas,
            #   buscar los indices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios.
            if select:
                index_ = [headers.index(column_name) for column_name in select]
                headers = select
            else:
                index_ = []

            for row in rows:
                # Saltea filas sin datos
                if not row:
                    continue
                # Filtrar la fila si se especificaron columnas
                if index_:
                    row = [row[index] for index in index_]
                # Si se especifica 'types' agrega type a las columnas
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # Genera el diccionario y lo agrega a la lista 'records'
                record = dict(zip(headers, row))
                records.append(record)

            return records

        else:
            for row in rows:
                if not row:
                    continue
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if select:
                    if select in row:
                        records.append(tuple(row))
                else:
                    records.append(tuple(row))
            # Solo se cumplira si se intenta filtrar con select y no existe la columna
            if len(records) == 0:
                print('Ingreso un registro que no existe en la lista')
            
            return records
