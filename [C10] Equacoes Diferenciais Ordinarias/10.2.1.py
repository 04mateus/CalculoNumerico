# Capítulo 10: equações diferenciais ordinárias
# circuito RL com fonte CC
#
# di/dt=f(i,t)=(1/L)(vm-ri)


import numpy as np
import matplotlib.pyplot as plt


V = 100
R = 10
L = 1
tf = 1
h = tf/100
it = 0
r = tf/h
i = np.zeros(1+int(r))
t = np.zeros(1+int(r))

while t[it] < tf:
    k1 = (1 / L) * (V - R * i[it])
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

plt.plot(t, i, linewidth=2)
plt.grid(True)
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.xlim(0, 1)
plt.ylim(0, 10)
plt.show()