# Ejercicio 7.9: Subplots fuera de una grilla
# plotGrilla.py

import matplotlib.pyplot as plt

fig = plt.figure()
# Define la figura de arriba
plt.subplot(2, 1, 1)
# Dibuja la curva
plt.plot([0, 1, 2], [0, 1, 0])
# Saca las marcas
plt.xticks([]), plt.yticks([])

# Define la primera de abajo, que sería la  cuarta si fuera una grilla regular de 2x2
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])
plt.xticks([]), plt.yticks([])

# Define la segunda de abajo, que sería la  quinta si fuera una grilla regular de 2x2
plt.subplot(2, 3, 5)
plt.plot([1, 0], [1, 1])
plt.xticks([]), plt.yticks([])

# Define la tercera de abajo, que sexta la  quinta si fuera una grilla regular de 2x2
plt.subplot(2, 3, 6)
plt.plot([0, 1], [1, 0])
plt.xticks([]), plt.yticks([])

plt.show()

