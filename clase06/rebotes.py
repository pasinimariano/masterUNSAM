# Ejercicio 1.5: La pelota que rebota
# rebotes.py


def rebotes():
    altura = 100  # medida expresada en mts
    rebotes = []  # se crea lista vacia donse se guardaran los rebotes que haga la pelota
    cantidad = 0  # especifica la cantidad de rebotes que se realizaron

    while len(rebotes) < 10:
        altura = round(altura / 5 * 3, 2)
        cantidad += 1
        tupla = cantidad, altura
        rebotes.append(tupla)

    return rebotes


def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        print(i)
    
incrementar([0,0,0,1,0,1])