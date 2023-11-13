# Capítulo 7: Ajuste de curvas
# Polinômios interpoladores de Newton

# importa a biblioteca necessária para a resolução do problema
import numpy as np
import matplotlib.pyplot as plt

# valores da curva de saturação
x = ([0.0000, 0.2500, 0.5000, 0.7500, 1.0000, 1.2500, 1.5000])
y = ([1.0000, 0.9689,  0.8776,  0.7317, 0.5403,  0.3153, 0.0707])
xx = 0.45000
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
print(f'yint = {yint:.4f}')  # Valor da interpolação para temp de 30 graus
# Comparação com funções nativas!
P = np.polyfit(x, y, 3)  # ajusta por mínimos quadrados um polinômio de n grau
s = np.polyval(P, xx)