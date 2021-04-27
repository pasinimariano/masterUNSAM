# Ejercicio 4.1: Debugger
# 4.1debugger.py


def invertir_lista(lista):
    '''Recibe una lista L y la devuelve invertida'''

    invertida = []
    i = len(lista) - 1

    while i >= 0:
        invertida.append (lista[i])
        i = i - 1
    
    return invertida

l = ['m', 'l', 3, 4, 'j']
m = invertir_lista(l)

print(f'Entrada: {l}, Salida: {m}')