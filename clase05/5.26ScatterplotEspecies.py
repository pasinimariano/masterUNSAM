# Ejercicio 5.26: Scatterplot para diferentes especies
# 5.26ScatterplotEspecies.py

import csv
import numpy as np
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):

    """ Se encargará de crear una lista, que contendrá todos los datos del archivo. 
    Cada dato estará almacenado en forma de diccionario. """

    archivo =  open(nombre_archivo, encoding='utf-8')
    cadenas = csv.reader(archivo)
    cabeceras = next(cadenas)

    registros = np.array([ items for items in cadenas ])
    data = np.array([ dict(zip(cabeceras, x)) for x in registros ])

    return data 


def medidas_de_especies(arboleda, lista_especies):

    """ Generara un diccionario, donde el key es la especie y el value es la altura y el diametro de dicha especie """
  
    medidas = np.array([ 
                {str(especie['nombre_com']) : (float(especie['altura_tot']), float(especie['diametro']))}
                for especie in arboleda 
                if str(especie['nombre_com']) in lista_especies ])
    
    return medidas

    

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
medidas = medidas_de_especies(arboleda, especies)

especie1 = [ arbol for arbol in medidas if especies[0] in arbol ]
altura1 = [ x[0] for y in especie1 for x in y.values() ]
diametro1 = [ x[1] for y in especie1 for x in y.values() ]
plt.scatter(altura1, diametro1, s = 25, c = 'green',  alpha = 0.40)
plt.xlabel('Alto (cm)')
plt.ylabel('Diametro (cm)')
plt.title(f'Relación diámetro-altura para {especies[0]}')
plt.xlim(0,30) 
plt.ylim(0,100)
plt.show()

especie2 = [arbol for arbol in medidas if especies[1] in arbol]
altura2 = [ x[0] for y in especie2 for x in y.values() ]
diametro2 = [ x[1] for y in especie2 for x in y.values() ]
plt.scatter(altura2, diametro2, s = 25, c = 'green',  alpha = 0.40)
plt.xlabel('Alto (cm)')
plt.ylabel('Diametro (cm)')
plt.title(f'Relación diámetro-altura para {especies[1]}')
plt.xlim(0,30) 
plt.ylim(0,100)
plt.show()

especie3 = [arbol for arbol in medidas if especies[2] in arbol]
altura3 = [ x[0] for y in especie3 for x in y.values() ]
diametro3 = [ x[1] for y in especie3 for x in y.values() ]
plt.scatter(altura3, diametro3, s = 25, c = 'green',  alpha = 0.40)
plt.xlabel('Alto (cm)')
plt.ylabel('Diametro (cm)')
plt.title(f'Relación diámetro-altura para {especies[2]}')
plt.xlim(0,30) 
plt.ylim(0,100)
plt.show()

plt.scatter(altura1, diametro1, s = 45, c = 'red',  alpha = 0.2, label = 'Eucalipto')
plt.scatter(altura2, diametro2, s = 45, c = 'green',  alpha = 0.2, label = 'Palo borracho rosado')
plt.scatter(altura3, diametro3, s = 45, c = 'violet',  alpha = 0.2, label = 'Jacarandá')
plt.xlabel('Alto (cm)')
plt.ylabel('Diametro (cm)')
plt.title(f'Relación diámetro-altura para {especies}')
plt.xlim(0,50) 
plt.ylim(0,50)
plt.show()
