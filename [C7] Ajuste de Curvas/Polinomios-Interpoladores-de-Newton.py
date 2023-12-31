# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Polinômios interpoladores de Newton


import numpy as np
import matplotlib.pyplot as plt


x = ([20, 25, 35])
y = ([1.12, 1.06, 0.94])  # PVC
# y = np.transpose([1.08, 1.04, 0.96])  # EPR
xx = 30
n = len(x)
b = np.zeros((n, n))
# atribui as variaveis dependentes à primeira coluna de b
b[:n, 0] = y[:]
for j in range(1, n):
    for i in range(0, n - j + 1):
        if i + j != n:
            b[i, j] = (b[i + 1, j - 1] - b[i, j - 1]) / (x[i + j] - x[i])
# usa as diferenças divididas finitas para interpolar
xt = 1
yint = b[0, 0]
for j in range(0, n - 1):
    xt = xt*(xx - x[j])
    yint = yint+b[0, j + 1] * xt
print(f'yint = {yint}')  # Valor da interpolação para temp de 30 graus
# Comparação com funções nativas!
P = np.polyfit(x, y, 2)  # ajusta por mínimos quadrados um polinômio de n grau
s = np.polyval(P, xx)
# gráfico
xp = np.linspace(min(x), max(x), 100)
ss = np.polyval(P, xp)
plt.plot(x, y, 'bo')
plt.plot(xx, yint, 'ro')  # plotagem de yint
# plt.plot(xx, s,'ro') # usando polyfit
plt.plot(xp, ss, 'k-')
plt.grid(True)
plt.show()