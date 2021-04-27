# Ejercicio 3.10: Invertir un diccionario
# invertir.py

precios = {
    'Pera' : 490.1,
    'Lima' : 23.45,
    'Naranja' : 91.1,
    'Mandarina' : 34.23
}

print('Items(): ', precios.items())

lista_precios = list(zip(precios.values(), precios.keys()))

print('Lista de precios: ', lista_precios)

print('Min: ', min(lista_precios))

print('Max: ', max(lista_precios))

print('Sorted: ', sorted(lista_precios))

a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]

print(list(zip(a, b, c)))

a = [1, 2, 3, 4, 5, 6]
b = ['w', 'x', 'y']

print(list(zip(a,b)))
