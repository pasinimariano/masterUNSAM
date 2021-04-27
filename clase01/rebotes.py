# Ejercicio 1.5: La pelota que rebota
# rebotes.py

altura = 100  # medida expresada en mts
rebotes = []  # se crea lista vacia donse se guardaran los rebotes que haga la pelota
cantidad = 0  # especifica la cantidad de rebotes que se realizaron

while len(rebotes) < 10:
    altura = round(altura / 5 * 3, 4)
    cantidad = cantidad + 1
    tupla = cantidad, altura
    rebotes.append(tupla)
    if len(rebotes) == 10:
        for x in rebotes:
            print(x)

