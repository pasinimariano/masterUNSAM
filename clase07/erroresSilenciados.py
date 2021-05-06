# Ejercicio 7.1: Errores silenciados
# erroresSilenciados.py

import csv


def parse_csv(file_name, select=None, types=None, silence_errors=False, has_headers=True):
    """
        Parsea un objeto en una lista de registros.
        -select, selecciona sólo un conjunto de columnas siempre y cuando tenga encabezados,
        sino dará error.
        -types, especifica el type de las columnas
        -silence_errors = True, silenciara los informes de errores.
        -has_headers, si no posee encabezados intercambiar a False.
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

                if not row:
                    continue
                # Filtrar la fila si se especificaron columnas
                try:
                    if index_:
                        row = [row[index] for index in index_]
                except UnboundLocalError:
                    break

                try:
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                except ValueError as vaEr:
                    if not silence_errors:
                        print(f'Fila {n_row}: No se puede convertir {row}')
                        print(f'Motivo: ', vaEr)

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
                    if not silence_errors:
                        print(f'Fila {n_row}: No se puede convertir {row}')
                        print(f'Motivo: ', vaEr)
                records.append(tuple(row))

            return records
