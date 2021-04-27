# Ejercicio 2.7: Buscar precios
# buscar_precios.py

print('Bienvenido. Este programa le dirá el precio de su producto')


def buscar_precio(nombre):
	f = open('Data/precios.csv', 'rt', encoding='utf-8')
	condicion = False

	for line in f:
		row = line.split(',')
		if row[0] == nombre:
			condicion = True
			precio = row[1]
	try:
		if condicion:
			print('El precio de %s es de: ' %nombre, precio) 
		elif len(nombre) <= 0:
			print('No ingreso ningun nombre')
		else:
			print('%s no figura en el listado de precios.' %nombre)

	except Exception as error:
			print('-------------------------------------------------------------------------')
			print('Surgio un error al cargar los datos, verifiquelos y vuelva a intentar.\n'
				'Error: ', error.args)
			print('-------------------------------------------------------------------------')
	


producto = input('Ingrese el producto: ').capitalize()
buscar_precio(producto)


