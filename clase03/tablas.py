# Ejercicio 3.17: Tablas de multiplicar
# tablas.py 


def tablas ():
    headers = '{0:>9}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}'
    numeros = '{0:>3}{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}'

    print(headers.format(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    print("-----------------------------------------------------")

    for num in range(0,10):
        print(numeros.format(str(num) + ':', num*0, num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9))


tablas()