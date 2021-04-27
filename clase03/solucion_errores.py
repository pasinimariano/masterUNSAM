# Ejercicios de errores en el código
# solucion_errores.py

#%%
# Ejercicio 3.1 Funcion tiene_a()
# Comentario: El problema es que si la primera letra no era una 'a', el programa salia por el Else y terminaba el bucle.

# Solución: Hay que realizar un return False fuera del bucle while, para que regrese False solo si recorre todo el string y no encuentra ninguna 'a'.

# Nuevo código:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    
    while i < n:

        if expresion[i] == 'a':
            return True
        i += 1
        
    return False

#%%
# Ejercicio 3.2: Sintasix
# Comentario: Existen varios problemas, faltan los ':' luego de la declaración de la funcion, lluego del bucle while y luego de la condición if.
#             También falta un '=' en la condición if. Por ultimo el return final debe ser el booleano False, y esta declarado como una variable Falso.

# Solución: Agregar los ':' faltantes, agregar el '=' faltante en la condición if, y por ultimo cambiar Falso, por False.

# Nuevo código:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

#%%
# Ejercicio 3.3: Tipos
# Comentario: El primer problema surge al intentar obtener una propiedad len de un int. El segundo error es que un int no puede ser analizado por el programa.

# Solucion: Primero agregar str luego de la propiedad len, para evitar errores de type.
#           El segundo error se puede solucionar estableciendo que el parametro que ingrese el usuario sea considerado siempre como un str.

# Nuevo código:

def tiene_uno(expresion):
    n = len(str(expresion))  
    str_expresion = str(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if str_expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

#%%
# Ejercicio 3.4: Alcances
# Comentario: El problema que surge en la función es que retorna none, al intentar realizar la suma.

# Solucion: Al final de toda funcion se debe realizar un return, para que devuelva el valor que se desee, en este caso 'c'.

# Nuevo código:

def suma(a,b):
    c = a + b
    return c

#%%
# Ejercicio 3.5: Pisando memoria
# Comentario: El problema es que cada vez que el bucle recorre la fila obtendra un registro nuevo, el cual modificará el key y el value de todo el diccionario. Esto genera que se solapen los datos.
#             'En cada iteración, el valor previo de la variable (si hubo alguno) es sobreescrito. Luego de terminar el ciclo, la variable retiene su último valor.'

# Solucion: Una solución sencilla sería crear un nuevo diccionario cada vez que el bucle recorra la fila, para luego almacenarlo en la lista. Así quedará una lista de diccionarios.    

# Nuevo código:

def leer_camion(nombre_archivo):
    camion=[]   
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict({encabezado[0] : fila[0],
                             encabezado[1] : fila[1],
                             encabezado[2] : fila[2]})
            camion.append(registro)
    return camion