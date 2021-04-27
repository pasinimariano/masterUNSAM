# Ejercicio 3.7: Más operaciones con secuencias
# operaciones_secuencias.py

data= [4, 9, 1, 25, 16, 100, 49]

print(min(data))

print(max(data))

print(sum(data))

for n in data:
    print(n)

for n, x in enumerate(data):
    print(n,x )

for n in range(len(data)):
        print(data[n])