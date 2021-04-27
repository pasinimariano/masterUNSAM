# Ejercicio 1.18: Geringoso rustico
# geringoso.py

cadena = 'Geringoso'
nueva_cadena = ''
vocales = 'AEIOUaeiuo'

for x in cadena:
    if x in vocales:
        nueva_cadena += x       # se agrega la letra a la nueva cadena
        nueva_cadena += 'p'     # agregar 'p' despues de la vocal
    nueva_cadena += x           # se repite la vocal

print('----------------------------------------------------------------------------')
print('Bienvenidx, puedo traducir cualquier palabra o frase a geringoso. Intentalo.')
print(cadena+':', nueva_cadena)
print('----------------------------------------------------------------------------')

usuario = str(input('Ingresa lo que desees traducir: '))
traduccion = ''

for x in usuario:
    if x in vocales:
        traduccion += x
        traduccion += 'p'
    traduccion += x

print('Original: ', usuario)
print('Traduccion: ', traduccion)


