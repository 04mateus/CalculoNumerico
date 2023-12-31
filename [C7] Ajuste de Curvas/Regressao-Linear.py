# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Regressão linear


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

x = np.transpose([0, 10, 20, 30, 40, 50, 70, 80, 90])
y = np.transpose([0, 10, 19, 31, 39, 52, 65, 69, 70])
n = len(x)  # número de amostras
if len(y) != n:
    print('x e y devem ter o mesmo tamanho')
sx = sum(x)
sy = sum(y)  # soma
sx2 = sum(x * x)
sxy = sum(x * y)
sy2 = sum(y * y)
a = np.zeros(2)
a[0] = (n * sxy - sx * sy) / (n * sx2 - sx ** 2)
a[1] = sy / n - a[0] * sx / n
r2 = ((n * sxy - sx * sy) / sqrt(n * sx2 - sx ** 2) / sqrt(n * sy2 - sy ** 2)) ** 2
r = sqrt(r2)
print(f'a = {a}')
# gráfico
xp = np.linspace(min(x), max(x), 2)
yp = a[0]*xp+a[1]
fig, ax = plt.subplots()
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y)+10)
eixo_y = np.linspace(min(y), max(y)+10, 5)
ax.set_yticks(eixo_y)
for c in eixo_y:
    c = str(c)
ax.set_yticklabels(eixo_y)
ax.plot(x, y, 'o', 'k', markersize=8)
ax.plot(xp, yp, 'k-', linewidth=2)
ax.grid(True)
ax.set_xlabel('V (V)')
ax.set_ylabel('I (A)')
V = 60
I = a[0] * V + a[1]
plt.show()