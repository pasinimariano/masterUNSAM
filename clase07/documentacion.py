# Ejercicio 7.8: Funciones y documentación
# documentacion.py

def valor_absoluto(n):
    """
        Devuelve el valor absoluto de un numero.
           Pre: 'n' debe ser un número real.
           Post: Se devuelve la distancia entre 'n' y 0, sin importar su signo.
    """
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(lista):
    """
        Recorre y suma los números pares de la lista.
            Pre: La lista debe ser de números.
            Post: Se devuelve la suma total de números pares.
    """
    # res: invariante de ciclo
    res = 0

    for e in lista:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    """
        Suma un numero 'a', 'b' cantidad de veces.
            Pre: 'a' puede ser entero o flotante. 'b' solo podrá ser entero.
            Post: Devolverá 'a' multiplicado por 'b'.
    """
    # res: invariante de ciclo
    res = 0
    nb = b

    while nb != 0:
        res += a
        nb -= 1

    return res


def collatz(n):
    """
        Comprueba la conjetura Collatz.
        La conjetura Collatz, establece que elijas el numero que se elijas siempre se llegará al 1.
            Pre: 'n' debe ser un entero.
            Post: Devuelve la cantidad de conversiones que se realizaron para llegar al 1.
    """
    # res: invariante de ciclo
    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

