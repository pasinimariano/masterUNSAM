# Ejercicio 1.19: Metodos de cadenas
# metodos.py

frutas = 'Manzana, Naranja, Mandarina, Banana, Kiwi'

print(frutas.lower())

print(frutas)

lowersyms = frutas.lower()

print(lowersyms)

print(frutas.find('Mandarina'))
print(frutas[13:17])

frutas = frutas.replace('Kiwi', 'Melon')
print(frutas)

nombre = '       Naranja \n'
nombre = nombre.strip()
print(nombre)