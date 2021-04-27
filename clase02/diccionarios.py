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

print('diccionario: ',d)

cost = d['cajones'] * d['precio']

print('costo: ', cost)

d['cajones'] = 75

print('cambio de value: ', d)

d['fecha'] = (13, 8, 2020)
d['cuenta'] = 12345

print('se agregan nuevos key-value: ', d)