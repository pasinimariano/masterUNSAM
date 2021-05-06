# Ejercicio 4.7: Búsqueda de máximo y mínimo
# 4.7MaxMin.py

def comparacion(lista):

    ''' Se encargará de mostrar el elemento más grande y el mas chico, de una lista de números'''

    num_max = lista[0]  # Primer item de la lista
    num_min = lista[0]  # Primer item de la lista

    for i in range(0, len(lista)): # Recorrera la lista completa
        if lista[i] >= num_max:    # Compara el elemento de la lista con el num_max
            num_max = lista[i]     # Si el elemento es mayor que el num_max, este último se reemplazará.
        if lista[i] <= num_min:    # Compara el elemento de la lista con el num_min
            num_min = lista[i]     # Si el elemento es menor que el num_min, este último se reemplazará.
        else:
            pass

    data = f'Max: {num_max}, Min: {num_min}'     
    
    return data


l1 = [1,2,7,2,3,4]
print('Lista a comparar: ', l1)
print(comparacion(l1))

print('------------------------------------------------------')

l2 = [1,2,7,2,3,4]
print('Lista a comparar: ', l2)
print(comparacion(l2))

print('------------------------------------------------------')

l3 = [-5,4]
print('Lista a comparar: ', l3)
print(comparacion(l3))

print('------------------------------------------------------')

l4 = [-5,-4]
print('Lista a comparar: ', l4)
print(comparacion(l4))

print('------------------------------------------------------')
