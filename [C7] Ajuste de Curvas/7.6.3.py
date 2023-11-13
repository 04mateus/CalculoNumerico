# Capítulo 7: Ajuste de Curvas
# SPLINES

# importa a biblioteca necessária para a resolução do problema
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sp

# definições das variáveis
def Spline(x_interp, x_pontos, fx_pontos):
    tck = sp.splrep(x_pontos, fx_pontos)
    return sp.splev(x_interp, tck)


def Pchip(x_interp, x_pontos, fx_pontos):
    pchip = sp.PchipInterpolator(x_pontos, fx_pontos)
    return pchip(x_interp)

# valores da tabela
tempo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tensao = [80, -60, 40, -30, 20, -10, 5, -2.5, 1.25, -0.625, 0.3125]
tt = 11

# imprime na tela
print(f'Interpolação Spline: y = {Spline(tt,tempo,tensao):.4f}')
print(f'Interpolação Pchip: y = {Pchip(tt,tempo,tensao):.4f}')

# plotagem do gráfico
plt.grid(True)
plt.plot(tempo, tensao, 'o', markersize=10, color='b')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')

# Comparação com funções nativas
P = np.polyfit(tempo, tensao, 3)  # ajusta por mínimos quadrados um polinômio de grau 3
xp = np.linspace(min(tempo), max(tempo), 100)
ss = np.polyval(P, xp)
plt.plot(xp, ss, 'r:', linewidth=2, label='polyfit grau 3')

P = np.polyfit(tempo, tensao, 5)  # ajusta por mínimos quadrados um polinômio de grau 5
ss = np.polyval(P, xp)
plt.plot(xp,  ss, 'g-.', linewidth=2, label='polyfit grau 5')

yy = Spline(x_interp=xp, x_pontos=tempo, fx_pontos=tensao)
plt.plot(xp, yy, 'k--', linewidth=4, label='Spline')
yy = Pchip(x_interp=xp, x_pontos=tempo, fx_pontos=tensao)
plt.plot(xp, yy, 'k', linewidth=2, label='Pchip')
plt.xlim(0, 10)
plt.ylim(-75, 75)
plt.tight_layout()

h = np.zeros(len(tempo)-1)
p = np.zeros(len(tempo)-1)
for i in range(0, (len(tempo) - 1)):
    h[i] = tempo[i + 1] - tempo[i]
    p[i] = (tensao[i + 1] - tensao[i]) / (tempo[i + 1] - tempo[i])

# utilização do método de interpolação
A = np.array([[1, 0, 0, 0, 0, 0],
             [h[0], 2*(h[0]+h[1]), h[1], 0, 0, 0],
             [0, h[1], 2*(h[1]+h[2]), h[2], 0, 0],
             [0, 0, h[2], 2*(h[2]+h[3]), h[3], 0],
             [0,  0, 0, h[3], 2*(h[3]+h[4]), h[4]],
             [0, 0, 0, 0, 0, 1]])

print(f'A =\n {A}')

pp = np.array([0, 3 * (p[1] - p[0]), 3 * (p[2] - p[1]), 3 * (p[3] - p[2]), 3 * (p[4] - p[3]), 0])
pp = np.transpose([pp])

c = np.linalg.lstsq(pp, A, rcond=None)[0][0]
b = np.zeros(len(tempo) - 1)
d = np.zeros(len(tempo) - 1)
print(f'pp =\n {pp}')
print(f'c =\n {c}')
#for i in range(0, (len(tempo) - 1)):
#    d[i] = (c[i + 1] - c[i]) / 3 * h[i]
print(f'd =\n {d}')
#for i in range(0, (len(tempo) - 1)):
#    b[i] = ((tensao[i + 1] - tensao[i]) / h[i]) - (h[i] / 3) * (2 * (c[i]) + c[i + 1])
print(f'b =\n {b}')
plt.legend()
plt.show()