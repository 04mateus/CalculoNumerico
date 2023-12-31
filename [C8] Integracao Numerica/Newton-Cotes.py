# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 8: Integração numérica
# Newton-Cotes


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def P(Vc, Ic):
    return np.multiply(Vc, Ic)


def ff(x):
    return (10 * np.exp(np.divide(-x, 0.001))) ** 2

R = 1
C = 0.001
Vo = 10
TAL = R * C
t = np.linspace(0, 3 * TAL, 7)
Vc = Vo * np.exp(np.divide(-t, (TAL)))
Ic = (Vo * np.exp(np.divide(-t, (TAL)))) / R
Pmed = Vo ** 2 / (6 * R) * (-np.exp(-6) + 1)
w = C * Vo ** 2 / 2 * (-np.exp(-6) + 1)
# trapézio
a = round(t[1])
b = t[len(t) - 1]
# limites
n = 150
# número de segmentos
x = a
h = (b - a) / n

Ianalitico = w
s = ff(x)
for i in range(0, n - 1):
    x = x + h
    s = s + 2 * ff(x)
s = s + ff(b)
P = (b - a) * s / (2 * n)
w = P
Pmed = w/(3 * TAL)
Erro = (Ianalitico - P)/Ianalitico
P = Vc * Ic
print('ff(x) = (10 * np.exp(np.divide(-x, 0.001))) ** 2 \n')
print(f'w = {w:.4f}')
print(f'Pmed = {Pmed:.4f}')
print(f'Erro = {Erro:.4f}')

# Visualização

Fig = plt.figure()
plt.style.use('fast')
ax1 = Fig.add_subplot(221)  # Posicionamento dos subplots
ax1.grid(True)  # grade
ax2 = Fig.add_subplot(222)  # Posicionamento dos subplots
ax2.grid(True)  # grade
ax3 = Fig.add_subplot(212)  # Posicionamento dos subplots
ax3.grid(True)  # grade

ax1.set_ylabel('V (V)')
ax2.set_ylabel('I (A)')
ax3.set_ylabel('P (W)')
ax3.set_xlabel('t (s) x10^-3')

ax1.locator_params(axis="y", nbins=2)
ax2.locator_params(axis="y", nbins=2)
ax3.locator_params(axis="y", nbins=2)

Tens = ax1.plot(t, Vc)
Corr = ax2.plot(t, Ic)
Pot = ax3.plot(t, P, label='T = 3RC')

ax1.set_xticklabels(['0', '1', '2', '3'])  # formatação do eixo x, V
ax2.set_xticklabels(['0', '1', '2', '3'])  # formatação do eixo x, I
ax3.set_xticklabels(['0', '0.5', '1', '1.5', '2', '2.5', '3'])  # formatação do eixo x, P

ax1.set_ylim(min(Vc), max(Vc))  # limite do eixo y, V
ax2.set_ylim(min(Ic), max(Ic))  # limite do eixo y, I
ax3.set_ylim(0, 100)  # limite do eixo y, P
ax1.set_xlim(0, 0.003)  # limite do eixo x, V
ax2.set_xlim(0, 0.003)  # limite do eixo x, I
ax3.set_xlim(0, 0.003)  # limite do eixo x, P
plt.legend()
plt.tight_layout()
plt.show()