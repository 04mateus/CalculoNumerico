# Capítulo 7: Ajuste de curvas
# Regressão polinômial

# importa a biblioteca necessária para a resolução do problema
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


Fig, ax = plt.subplots()
ax.grid(True)
# tabela com os valores de resistência e corrente
x = np.transpose([1, 1.1, 1.25, 1.5, 2, 2.2, 3.5, 5, 6, 6.5, 7, 8, 8.75, 9.5, 10])
y = np.transpose([10, 9, 8.9, 7, 6, 5.5, 4, 2, 1.5, 1.1, 1.05, 1, 1, 1.1, 0.95])
n = len(x)  # número de amostras
sx = sum(x)
sy = sum(y)  # soma
mx = sx/n
my = sy/n
# equações para os cálculos necessários
sx2 = sum(x * x)
sx3 = sum(x * x * x)
sx4 = sum(x * x * x * x)
sxy = sum(x * y)
sx2y = sum(x * x * y)
x = [1, 1.1, 1.25, 1.5, 2, 2.2, 3.5, 5, 6, 6.5, 7, 8, 8.75, 9.5, 10]
y = [10, 9, 8.9, 7, 6, 5.5, 4, 2, 1.5, 1.1, 1.05, 1, 1, 1.1, 0.95]
A = np.array([[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]])
b = np.transpose([sy, sxy, sx2y])
c = np.linalg.lstsq(A, b, rcond=None)[0]
yy = sum(np.power((y-my), 2))
yyy = 0
for i in range(0, n):
    yyy = yyy + (y[i] - c[0] - c[1]*x[i] - c[2] * x[i] ** 2) ** 2

r2 = (yy - yyy) / yy
r = sqrt(r2)
V = 30
I = c[0] + c[1] * V + c[2] * np.power(V, 2)
# plotagem do gráfico e equações
xx = np.linspace(min(x), max(x), 100)
yy = c[0] + c[1] * xx + c[2] * np.power(xx, 2)
ax.plot(xx, yy, label='grau 3')
ax.plot(x, y, 'o', label="(x,y)")
ax.set_xlabel('R (Ohms)')
ax.set_ylabel('I (A)')

plt.tight_layout()
plt.legend()
plt.show()