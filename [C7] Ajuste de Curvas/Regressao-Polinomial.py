# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Regressão polinômial


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


Fig, ax = plt.subplots()
ax.grid(True)
x = np.transpose([0, 10, 20, 30, 40, 50, 70, 80, 90])
y = np.transpose([0, 10, 19, 31, 39, 52, 65, 69, 70])
n = len(x)  # número de amostras
sx = sum(x)
sy = sum(y)  # soma
mx = sx/n
my = sy/n
sx2 = sum(x * x)
sx3 = sum(x * x * x)
sx4 = sum(x * x * x * x)
sxy = sum(x * y)
sx2y = sum(x * x * y)
x = [0, 10, 20, 30, 40, 50, 70, 80, 90]
y = [0, 10, 19, 31, 39, 52, 65, 69, 70]
# [A]{c} = {b}
A = np.array([[n, sx, sx2], [sx, sx2, sx3], [sx2, sx3, sx4]])
b = np.transpose([sy, sxy, sx2y])
c = np.linalg.lstsq(A, b, rcond=None)[0]  # resolução de sistemas
yy = sum(np.power((y-my), 2))             # rcond=None: versão mais atualizada
yyy = 0
for i in range(0, n):
    yyy = yyy + (y[i] - c[0] - c[1]*x[i] - c[2] * x[i] ** 2) ** 2

r2 = (yy - yyy) / yy
r = sqrt(r2)
V = 30
I = c[0] + c[1] * V + c[2] * np.power(V, 2)
# gráfico
xx = np.linspace(min(x), max(x), 100)
yy = c[0] + c[1] * xx + c[2] * np.power(xx, 2)
ax.plot(xx, yy, label='pol grau 2')
ax.plot(x, y, 'o', label="(x,y)")
ax.set_xlabel('V (V)')
ax.set_ylabel('I (A)')

plt.tight_layout()
plt.legend()
plt.show()