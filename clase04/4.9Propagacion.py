# Ejercicio 4.9: Propagación
# 4.9Propagacion.py


def invertir_lista(lista):

    ''' Recibe una lista y la devuelve invertida '''

    invertida = []
    i = len(lista) - 1 # Se resta 1 para obtener la última posición de la lista.

    while i >= 0:
        invertida.append(lista[i]) # Se agrega el último elemento de la lista.
        i = i - 1

    return invertida

def siguiente_elem(l):

    """ Verifica una lista y verifica el elemento posterior """

    for index, elem in enumerate(l):
        try:
            if elem == 1 and l[index + 1] == 0:   
                l[index + 1] = 1  
            else:
                pass
        except IndexError:
            break

def propagar(array):

    """ El programa recorrera la lista, y si encuentra un 1 adyacente a un 0,
     este último será convertido en un 1. """

    # Invierte el orden de la lista.
    invertida = invertir_lista(array)  
    siguiente_elem(invertida)
             
    # Se vuelve la lista a su orden original.
    propagada = invertir_lista(invertida)
    siguiente_elem(propagada)

    return propagada


l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0 ]
propagar1 = propagar(l1)
print('Original:  ', l1)
print('Propagada: ', propagar1)

print('------------------------------------------------------')

l2 = [ 0, 0, 0, 1, 0, 0 ]
propagar2 = propagar(l2)
print('Original:  ', l2)
print('Propagada: ', propagar2)

print('------------------------------------------------------')
    
l3 = [ 0, 0, -1, 0, 0, 1 ]
propagar3 = propagar(l3)
print('Original:  ', l3)
print('Propagada: ', propagar3)

print('------------------------------------------------------')

l4 = [ 0, -1, 1, 0, -1, 0 ]
propagar4 = propagar(l4)
print('Original:  ', l4)
print('Propagada: ', propagar4)
