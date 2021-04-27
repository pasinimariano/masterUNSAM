# Ejercicio 7.0: Manejo de except en FileParse.py
# exceptFileParse.py

import csv


def parse_csv(file_name, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un conjunto de columnas, determinando el parametro 'select':
        -en el caso de que posea encabezados, debe ser una lista de nombres de las columnas a considerar.
        -en el caso que no posea encabezados, generará un RuntimeError y el usuario será notificado.
    Tambien se puede especificar el type de los datos de cada columna, utilizando el
    parametro 'types', en forma de lista por cada columna.
    Por ultimo si el archivo no posee encabezados se debe especificar utilizando el parametro
    'has_headers = False'. Si no los posee no es necesario pasarle este parametro.
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
            try:
                if select:
                    index_ = [headers.index(column_name) for column_name in select]
                    headers = select
                else:
                    index_ = []
            except ValueError:
                print(f'Uno o más encabezados no existen en el archivo {file_name}')

            for n_row, row in enumerate(rows):
                # Saltea filas sin datos
                if not row:
                    continue
                # Filtrar la fila si se especificaron columnas
                try:
                    if index_:
                        row = [row[index] for index in index_]
                except UnboundLocalError:
                    break
                # Si se especifica 'types' agrega type a las columnas
                try:
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                except ValueError as vaEr:
                    print(f'Fila {n_row}: No se puede convertir {row}')
                    print(f'Motivo: ', vaEr)
                # Genera el diccionario y lo agrega a la lista 'records'
                record = dict(zip(headers, row))
                records.append(record)

            return records

        else:
            if not has_headers and select is not None:
                raise RuntimeError("Para utilizar 'select', necesito encabezados.")
            for n_row, row in enumerate(rows):
                if not row:
                    continue
                try:
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                except ValueError as vaEr:
                    print(f'Fila {n_row}: No se puede convertir {row}')
                    print(f'Motivo: ', vaEr)
                records.append(tuple(row))

            return records
