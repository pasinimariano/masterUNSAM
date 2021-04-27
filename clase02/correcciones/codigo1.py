#2.18: Balances

import csv

def leer_camion(archivo):
    "Guarda los datos de un camión (producto, cant. de cajas, precio por caja), situados en 'archivo', en una lista de diccionarios"
    camion = []                                            #abro lista de diccionarios
    
    with open(archivo,'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)                               #salteo los encabezados
        for row in rows:
        
            try:
                nombre = row[0]
                n_cajones = int(row[1])
                precio = float(row[2])
                lote = {'nombre': nombre, 'cajones': n_cajones, 'precio': precio}
                camion.append(lote)                                                  #agrego el lote a la lista
                
            except:
                print(f'El producto {nombre} no tiene toda la información necesaria.')
    
    return(camion)

def leer_precios(archivo):
    "Guarda los datos de venta (producto, precio por caja), situados en 'archivo', en un diccionario"
    precios = {}                                             #abro diccionario
    n_rows = 0                                               #contador para detectar líneas vacías

    with open(archivo,'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        for row in rows:
            print(row)
            n_rows += 1        
            try:
                nombre = row[0]
                precio = float(row[1])
                precios[nombre] = precio                     #agrego nueva entrada clave-valor al diccionario 
 
            except:
                print(f'La línea {n_rows} del archivo {archivo} no contiene información.')

    
    return(precios)

#costo del camion
costo = 0.0
camion = leer_camion('Data/camion.csv')
for i in camion:
    costo += i['cajones'] * i['precio']

#ganancia en lugar de descarga
recaudacion = 0.0
precio_venta = leer_precios('Data/precios.csv')
for i in camion:
    producto = i['nombre']
    recaudacion += i['cajones'] * precio_venta[producto]

balance = recaudacion - costo
print(f'El costo del camion fue de ${costo: .2f}, su recaudación en el lugar de venta fue de ${recaudacion: .2f} y su balance fue de ${balance: .2f}.')
#La línea 31 del archivo ../Data/precios.csv no contiene información.
#El costo del camion fue de $ 47671.15, su recaudación en el lugar de venta fue de $ 62986.10 y su balance fue de $ 15314.95.