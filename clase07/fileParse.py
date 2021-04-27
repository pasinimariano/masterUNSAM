# Ejercicio 7.4: De archivos a "objetos cual archivos"
# fileParse.py


def parse_interable(objeto, select=None, types=None, silence_errors=False, has_headers=True):
    """
    Parsea un objeto en una lista de registros.
    Se puede seleccionar sólo un conjunto de columnas, determinando el parametro 'select':
        -en el caso de que posea encabezados, debe ser una lista de nombres de las columnas a considerar.
        -en el caso que no posea encabezados, generará un RuntimeError y el usuario será notificado.
    Tambien se puede especificar el type de los datos de cada columna, utilizando el
    parametro 'types', en forma de lista por cada columna.
    Si se especifica el parametro 'silence_errors = True', silenciara los informes de errores en el
    parseo de los datos.
    Por ultimo si el objeto no posee encabezados se debe especificar utilizando el parametro
    'has_headers = False'. Si los posee no es necesario pasarle este parametro.
    """

    records = []

    if has_headers:
        # Lee los encabezados
        # Al realizar el split python genera un '\n' automatico
        #   se utiliza replace para eliminarlo.
        iterator = iter(objeto)
        headers = next(iterator).replace('\n', '').split(',')
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
            print(f'Uno o más encabezados no existen')

        for n_row, row in enumerate(objeto[1:]):
            row = row.replace('\n', '').split(',')
            if row == headers:
                pass
            # Saltea filas sin datos
            if not row:
                continue
            # Filtrar la fila si se especificaron columnas
            try:
                if index_:
                    row = [row[index] for index in index_]
            except UnboundLocalError:
                break
            # Si se especifica 'types' agrega type a las filas
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as vaEr:
                if not silence_errors:
                    print(f'Fila {n_row}: No se puede convertir {row}')
                    print(f'Motivo: ', vaEr)
            # Genera un diccionario y lo agrega a la lista 'records'
            record = dict(zip(headers, row))
            records.append(record)

        return records

    else:
        if not has_headers and select is not None:
            raise RuntimeError("Para utilizar 'select', se necesita encabezados.")
        for n_row, row in enumerate(objeto):
            row = row.replace('\n', '').split(',')
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
