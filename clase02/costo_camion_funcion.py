f = open('../Data/camion.csv', 'rt')
headers = next(f).split(', ')
precios = []

for line in f:
	row = line.split(',')
	precio_cajones = float(row[1]) * float(row[2])
	precios.append(precio_cajones)

precio_total = sum(precios)
print('Costo Total: ', precio_total)


def costo_camion(nombre_archivo):
	f = open(nombre_archivo)
	next(f).split(',')
	precios = []
	
	for line in f:
		row = line.split(', ')
		precio_cajones = float(row[1]) * float(row[2])
		precios.append(precio_cajones)
	
	precio_total = sum(precios)
	return precio_total


costo = costo_camion('../Data/camion.csv')
print('Costo Total, desde la funcion: ', costo)