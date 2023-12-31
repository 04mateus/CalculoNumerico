# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Polinômios interpoladores de Lagrange


import matplotlib.pyplot as plt
import numpy as np


x = ([20, 25, 35])
y = ([1.12, 1.06, 0.94])  # PVC
# y = ([1.08, 1.04, 0.96])  # EPR
xx = 30
n = len(x)  # número de amostras
if len(y) != n:
    print('x e y devem ter o mesmo tamanho')
s = 0
for i in range(0, n):
    produto = y[i]
    for j in range(0, n):
        if i != j:
            produto = produto * (xx - x[j]) / (x[i] - x[j])
    s = s + produto
print(f's = {s}')

# gráfico
plt.grid(True)
c = np.polyfit(x, y, 2)
x_polyfit = np.linspace(min(x), max(x), 100)
y_polyfit = np.polyval(c, x_polyfit)
plt.plot(x_polyfit, y_polyfit, 'k')
plt.plot(x, y, 'bs')
plt.plot(xx, s, 'ro')
plt.show()