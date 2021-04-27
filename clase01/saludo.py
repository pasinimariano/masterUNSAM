# Ejercicio 1.6: Saludos
# saludo.py

nombre= input('Por favor ingresa tu nombre: ')

saludo = "Bienvenido nuevamente: " + nombre

print(saludo)

lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
headers = lines[0]
index_ = [headers.index(column_name) for column_name in select]