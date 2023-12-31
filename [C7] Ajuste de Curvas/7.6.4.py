# Capítulo 7: Ajuste de curvas
# Curvas Senoidais

# importa a biblioteca necessária para a resolução do problema
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import pi

MAX = [10, 50, 100]
ts = []
xx = np.zeros((len(MAX), 1000))

Fig = plt.figure()
axes = []

for i in range(0, len(MAX)):
    nMax = MAX[i]

    f = 60
    div = 6  # divisor de pi, gera o angulo onde ocorre a descontinuidade.
    Vmax = 311
    T = 1 / f
    w = 2 * pi * f
    pxt = 1000  # resolução

    a0 = (Vmax / pi) * (np.cos(pi / div) - np.cos(pi))

    t = np.linspace(0, T, pxt)
    t = np.array([t])

    n = np.linspace(1, nMax, nMax)
    n = n.reshape(nMax, 1)

    cosnt = np.cos(np.dot(n, t) * 4 * pi * f)
    sinnt = np.sin(np.dot(n, t) * 4 * pi * f)
    n = 0

    # cálculo necessário para a equação num laço de repetição
    ann = np.array([])
    bnn = np.array([])
    while n < (nMax + 1):
        if n != 0:
            ann = np.append(ann, (Vmax / pi) * (
                        ((np.cos(pi * (2 * n - 1)) - (np.cos(pi * (2 * n - 1) / div))) / (2 * n - 1)) + (
                            (np.cos(pi * (2 * n + 1) / div) - (np.cos(pi * (2 * n + 1)))) / (2 * n + 1))))
            bnn = np.append(bnn, (Vmax / pi) * (
                        ((np.sin(pi * (2 * n - 1)) - (np.sin(pi * (2 * n - 1) / div))) / (2 * n - 1)) + (
                            (np.sin(pi * (2 * n + 1) / div) - (np.sin(pi * (2 * n + 1)))) / (2 * n + 1))))
        n = n + 1

    soma = np.dot(ann, cosnt) + np.dot(bnn, sinnt)  # faz uma soma dos valores
    xt = a0 + soma  # define Xt

    xx[i, :] = xt
    ts.append(t[0])

    axes.append(Fig.add_subplot(f'{len(MAX)}1{i + 1}'))

for index in range(0, len(axes)):
    axes[index].plot(ts[index], xx[index, :], 'k-', linewidth=2, label=f'N={MAX[index]}')
    axes[index].set_ylabel('V (V)')
    axes[index].set_xlim([0, T])
    axes[index].set_ylim([-20, 320])
    axes[index].grid(True)
    axes[index].legend(loc='upper right')

plt.tight_layout()

plt.show()