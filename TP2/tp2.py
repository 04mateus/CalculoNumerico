# Capítulo 10: EDO
# Aluno: Mateus Salgado Barboza Costa
# Circuito RL com fonte CC

import numpy as np
import matplotlib.pyplot as plt

V = 60 # tensão fonte CC
R = 12 # resistência R
L = 4 # indutância L
tf = 4.9 # tempo final
h = tf/100 # quantidade de pontos

it = 0
r = tf/h
i = np.zeros(1+int(r))
t = np.zeros(1+int(r))
while t[it] < tf:
    k1 = (1 / L) * (V - R * i[it]) # EDO
    tx = t[it] + (1 / 2) * h
    ix = i[it] + (1 / 2) * k1 * h
    k2 = (1 / L) * (V - R * ix)
    tx = t[it] + (1 / 2) * h
    ix = i[it] + (1 / 2) * k2 * h
    k3 = (1/L) * (V - R * ix)
    tx = t[it] + h
    ix = i[it] + k3 * h
    k4 = (1 / L) * (V - R * ix)
    i[it + 1] = i[it] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h
    t[it + 1] = t[it] + h
    it += 1

# Visualização
print(f"Valor da corrente i(5) = {i[100]} A") # Resultado

plt.plot(t, i, linewidth=2)
plt.grid(True)
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.xlim(0, 5)
plt.ylim(0, 6)
plt.show()