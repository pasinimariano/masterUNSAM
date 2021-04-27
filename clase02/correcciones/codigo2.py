import csv

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_rows, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            record['cajones']=int(record['cajones'])
            record['precio']=float(record['precio'])
            camion.append(record)
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precios={}
        rows=csv.reader(f)
        for row in rows:
             try:
                 precios[row[0]]=float(row[1])
             except:
                 print()
        return precios

precios=leer_precios('Data/precios.csv')
camion=leer_camion('Data/camion.csv')
frutas=[]
invertido=0.0
obtenido=0.0
for cajones in camion:
    invertido+=cajones['cajones']*cajones['precio']
    if cajones['nombre'] in precios:
        obtenido+= cajones['cajones']*precios[cajones['nombre']]
if invertido < obtenido:
    print('Hubo Ganancia. Dinero invertido= $', invertido, 'Dinero obtenido= $', obtenido, 'Ganancia= $', round(obtenido - invertido, 2))
elif invertido > obtenido:
    print('Hubo pérdida. Dinero invertido= $', invertido, 'Dinero obtenido= $', obtenido, 'Pérdida= $', round(obtenido - invertido, 2))
else:
    print('No hubo ganancia')