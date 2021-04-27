f = open('Data/camion.csv', 'rt')
headers = next(f).split(', ')
precios = []

for line in f:
	row = line.split(', ')
	precio_cajones = float(row[1]) * float(row[2])
	precios.append(precio_cajones)

precio_total = sum(precios)
print('Costo Total: ', precio_total)
