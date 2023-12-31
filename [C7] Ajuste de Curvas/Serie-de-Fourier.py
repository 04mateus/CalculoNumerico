# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 7: Ajuste de curvas
# Série de Fourier


import numpy as np


pi = np.pi
T = 1 / 60
t = np.linspace(0, T, 9)
y = np.array([0, 220, 311, 220, 0, -220, -311, -220, 0])
n = len(t)
print(np.fft.fft(y, n - 1))  # fast Fourier - transform
# np.fft.ifft(y, n - 1)  # Descomentar para usar inverse fast Fourier - transform