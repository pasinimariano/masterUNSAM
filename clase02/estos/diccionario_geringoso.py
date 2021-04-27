# Ejercicio 2.14: Diccionario geringoso.
# diccionario_geringoso.py

elements = ['Manzanas', 'Bananas', 'Mandarinas', 'Pera']
nueva_cadena = ''
vocales = 'AEIOUaeiuo'


def traducir_lista(keys):
    global nueva_cadena
    separador = '#'.join(keys)          # se agrega '#' entre cada palabra
    
    for items in separador:
        for x in items:
            if x in vocales:
                nueva_cadena += x       # se agrega la letra a la nueva cadena
                nueva_cadena += 'p'     # agregar 'p' despues de la vocal
            nueva_cadena += x           # se repite la vocal 

    values = nueva_cadena.split('#')    # se separa las palabras cuando aparece '#'
    diccionario_traducciones = dict(zip(keys,values)) # se crea un diccionario 

    return diccionario_traducciones

print(traducir_lista(elements))