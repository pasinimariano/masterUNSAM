# Ejercicio 4.8: Invertir una lista
# 4.8Invertir.py


def invertir_lista(lista):

    ''' Recibe una lista y la devuelve invertida '''

    invertida = []
    i = len(lista) - 1 # Se resta 1 para obtener la última posición de la lista.

    while i >= 0:
        invertida.append(lista[i])
        i = i - 1

    return invertida


l = [1, 2, 3, 4, 5]
m = invertir_lista(l)

print(f'Entrada: {l}\nSalida: {m}')
print('--------------------------------------------------------------')

l2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
m2 = invertir_lista(l2)

print(f'Entrada: {l2}\nSalida: {m2}')
print('--------------------------------------------------------------')