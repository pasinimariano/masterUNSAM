# Ejercicio 5.2: Generala
# 5.2Generala.py

import random


def tirada():

    """ Generará una lista con 5 números aleatorios """

    tirada = [ random.randint(1, 6) for x in range(5) ]

    return tirada
    

def generala(tirada, tirada2, tirada3):

    """ Manipulara los resultados obtenidos de las tiradas, e intentará 
    llegar a obtener una generala (todos los numeros iguales) """

    # Si todos los elementos de la tirada son iguales devolverá True.
    servida = len(tirada) > 0 and all(elem == tirada[0] for elem in tirada) 

    if servida == False:
        # Comprueba si hay elementos repetidos
        dados = [ i for i in tirada if tirada.count(i) > 1 ]
        
        # Intento 2 
        if len(dados) == 0:
            # La segunda tirada es servida?
            servida2 = len(tirada2) > 0 and all(elem == tirada2[0] for elem in tirada2)

            if servida2 == False:
                # Comprueba si hay elementos repetidos
                dados2 = [ i for i in tirada2 if tirada2.count(i) > 1 ] 

                # Intento 3
                if len(dados2) == 0:
                    # La tercera tirada es servida?
                    servida3 = len(tirada3) > 0 and all(elem == tirada3[0] for elem in tirada3)

                    return servida3
                
                else:
                    # Separa los elementos repetidos en la tirada
                    dados3 = [ e for e in dados2 if e == dados2[0] ]
                    repetidos = len(dados3)
                    # Genera nuevos numeros restando los repetidos
                    nuevos = [ random.randint(1, 6) for x in range(5 - repetidos) ]
                    # Une los repetidos con los nuevos
                    mano = dados3 + nuevos
                    # Si todos los elementos de la tirada son iguales devolverá True.                  
                    generala = len(mano) > 0 and all(elem == mano[0] for elem in mano) 

                    return generala

            else:
                return servida2

        else:
            # Separa los elementos repetidos en la tirada
            dados2 = [ e for e in dados if e == dados[0] ]
            repetidos = len(dados)
            # Genera nuevos numeros restando los repetidos
            nuevos = [ random.randint(1, 6) for x in range(5 - repetidos) ]
            # Une los repetidos con los nuevos
            mano = dados2 + nuevos
            # Si todos los elementos de la tirada son iguales devolverá True.                  
            generala = len(mano) > 0 and all(elem == mano[0] for elem in mano) 

            if generala:
                return generala

            # Intento 3 
            else:
                # Separa los elementos repetidos en la tirada
                dados3 = [ e for e in mano if e == mano[0] ]
                repetidos = len(dados)
                # Genera nuevos numeros restando los repetidos
                nuevos = [ random.randint(1, 6) for x in range(5 - repetidos) ]
                # Une los repetidos con los nuevos
                mano = dados3 + nuevos
                # Si todos los elementos de la tirada son iguales devolverá True.                  
                generala = len(mano) > 0 and all(elem == mano[0] for elem in mano) 

                return generala

    else:
        return servida


tiradas = 1000000
dados, dados2, dados3 = tirada(), tirada(), tirada()
generala = [ generala(dados, dados2, dados3) for _ in range(tiradas) ]
gano = [ i for i in generala if i ]
promedio = len(gano) / tiradas


print(f'Tire {tiradas} veces, de las cuales {len(gano)} veces saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala es de {promedio:.6f}.')