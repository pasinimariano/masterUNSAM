# Ejercicio 4.10: Compernsion de listas
# 4.10Compresion.py

nums = [1, 2, 3, 4]

cuadrados = [x * x for x in nums]

print(cuadrados)

dobles = [2 * x for x in nums if x > 2]

print(dobles)