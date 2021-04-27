# Ejercicio 5.20: Plotear el histograma
# 5.20PlotearFiguritas.py

import matplotlib.pyplot as plt
import numpy as np


figuritas_unidad = np.load('../Data/Figuritas.npy')
plt.hist(figuritas_unidad, bins= 40)
plt.xlabel("Figuritas compradas")
plt.ylabel("Frecuencia")
plt.title("Figurita por unidad")
plt.show()

figuritas_paquete = np.load('../Data/Figuritas1.npy')
plt.hist(figuritas_paquete, bins= 5)
plt.xlabel("Paquetes comprados")
plt.ylabel("Frecuencia")
plt.title("Figurita por paquete (5)")
plt.show()

