# Ejercicio 7.6: Sumas
# sumarEnteros.py

# Utilizando un loop
def sumar_enteros_loop(desde, hasta):
    """
        Calcula la sumatoria de los números entre 'desde y hasta'.
        Si hasta < desde, entonces devuelve 0.

         Pre: desde y hasta son números enteros
         Pos: Se devuelve el valor de sumar todos los números del intervalo
            [desde, hasta]. Si el intervalo es vacío se devuelve 0
    """
    # Invariante de ciclo
    sumatoria = 0

    if isinstance(desde, int) and isinstance(hasta, int):
        while desde <= hasta:
            sumatoria = sumatoria + desde
            desde += 1

    else:
        print('Ambos parametros deben ser numeros enteros')

    return sumatoria


# Sin utilizar loop
def sumar_enteros(desde, hasta):
    """
        Calcula la sumatoria de los números entre 'desde y hasta'.
        Si hasta < desde, entonces devuelve 0.

         Pre: desde y hasta son números enteros
         Pos: Se devuelve el valor de sumar todos los números del intervalo
            [desde, hasta]. Si el intervalo es vacío se devuelve 0
    """
    sumatoria = 0

    if isinstance(desde, int) and isinstance(hasta, int):
        if hasta > desde:
            n = len(range(desde, hasta + 1))
            sumatoria = ((desde + hasta) * n) // 2
    else:
        print('Ambos parametros deben ser numeros enteros')

    return sumatoria
