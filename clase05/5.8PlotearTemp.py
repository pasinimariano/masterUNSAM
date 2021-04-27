# Ejercicio 5.8: Empezando a plotear
# 5.8PlotearTemp.py

import matplotlib.pyplot as plt
import numpy as np


temperaturas = np.load('../Data/Temperaturas.npy')
plt.hist(temperaturas, bins = 50)
plt.xlabel('Temperaturas')
plt.ylabel('Frecuencias')
plt.title('Temperatura: 37.5')
plt.show()