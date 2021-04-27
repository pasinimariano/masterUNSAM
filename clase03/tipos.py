# Ejercicio 3.3: Tipos
# tipos.py

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


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))