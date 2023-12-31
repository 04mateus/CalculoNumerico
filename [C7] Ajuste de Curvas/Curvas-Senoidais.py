# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Curvas Senoidais


from numpy import array, linspace, zeros
from math import pi, cos, sin
import matplotlib.pyplot as plt


def yfunc(t):
    return 0 + 311 * sin(w * t + 0)


T = 1 / 60
t = linspace(0, T, 9)
w = 2 * pi * 60
n = len(t)
m = 3
y = array([0, 220, 311, 220, 0, -220, -311, -220, 0])
sy = sum(y)
A0 = sy / n
A = zeros(m + 1)
B = zeros(m + 1)
f = zeros((m, n))
ff = zeros((n, n))
ycos = zeros(n)
ysin = zeros(n)
for k in range(0, m + 1):
    for i in range(0, n):
        ycos[i] = (y[i] * cos(k * w * t[i]))
        ysin[i] = (y[i] * sin(k * w * t[i]))
    A[k] = (2 / n) * sum(ycos)
    B[k] = (2 / n) * sum(ysin)
for k in range(0, m):
    for i in range(0, n):
        f[k, i] = A[k] * cos(k * w * t[i]) + B[k] * sin(k * w * t[i])
for i in range(0, n):
    ff[i] = A0 + sum(f[:, i])
A = A[1:]
B = B[1:]

Fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(t, y, 'o', markersize=10, color='b', label='9 pontos medidos')
ffplot = []
for c in ff:
    ffplot.append(c[0])
ff = ffplot
ax.plot(t, ff, 'rs', label='m = 3 para 9')
T = 1 / 60
t = linspace(0, T, 120)
w = 2 * pi * 60
n = len(t)
m = 3

sy = sum(y)
A0 = sy / n
A = zeros(m + 1)
B = zeros(m + 1)
f = zeros((m, n))
ff = zeros((n, n))
ycos = zeros(n)
ysin = zeros(n)
for k in range(0, m + 1):
    for i in range(0, n):
        ycos[i] = (yfunc(t[i]) * cos(k * w * t[i]))
        ysin[i] = (yfunc(t[i]) * sin(k * w * t[i]))
    A[k] = (2 / n) * sum(ycos)
    B[k] = (2 / n) * sum(ysin)
for k in range(0, m):
    for i in range(0, n):
        f[k, i] = A[k] * cos(k * w * t[i]) + B[k] * sin(k * w * t[i])
for i in range(0, n):
    ff[i] = A0 + sum(f[:, i])
A = A[1:]
B = B[1:]
ffplot = []
for c in ff:
    ffplot.append(c[0])
ff = ffplot
ax.plot(t, ff, 'k', label='m = 3 para 120')
ax.legend()
ax.grid(True)
ax.set_xlim(min(t) - 0.00015, max(t) + 0.00015)  # Ajuste de visualização do gráfico
ax.set_ylim(min(ff) - 12, max(ff) + 12)  # Ajuste de visualização do  gráfico
ax.set_ylabel('V (V)')
ax.set_xlabel('Tempo (s)')
plt.show()