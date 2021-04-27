import csv

f = open('Data/camion.csv')
rows = csv.reader(f)
next(rows)
fila = next(rows)

d = {
    'nombre' : fila[0],
    'cajones' : int(fila[1]),
    'precio' : float(fila [2])
}

for k in d: 
    print('k =', k)


for k in d:
    print(k, '=', d[k])


items = d.items()
print('items: ', items)

for k, v in d.items():
    print(k, '=', v)

print('lista del diccionario: ', list(d))

claves= d.keys()

print('claves: ', claves)


nuevos_items = [('nombre', 'Manzanas'), 
                ('cajones', 100), 
                ('precio', 490.1), 
                ('fecha', (13, 8, 2020))]

print(nuevos_items)

d= dict(nuevos_items)

print(d)