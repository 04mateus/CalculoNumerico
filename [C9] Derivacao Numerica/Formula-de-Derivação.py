# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 9: Derivação numérica
# RL


from numpy import divide, diff
import matplotlib.pyplot as plt


t = [0, 0.10, 0.20, 0.30, 0.40, 0.50]
I = [0, 1.00, 3.00, 5.00, 8.50, 20.00]
d = divide(diff(I), diff(t))
L = 0.1
V = L * d
tt = [0.05, 0.15, 0.25, .35, .45]

print(f'd = {d}\n')
print(f'V = {V}\n')

# Visualização
fig, ax = plt.subplots()
Corr = ax.plot(t, I, linewidth=1, marker='d', label='Corrente')
ax2 = ax.twinx()  # cria nova escala no lado oposto do gráfico eixo y
Tens = ax2.plot(tt, V, linewidth=1, marker='s', label='Tensão', linestyle='--', color='k')
lns = Tens + Corr
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Corrente (A)')
ax2.set_ylabel('Tensão (V)')
ax2.yaxis.grid(False)
plt.tight_layout()
plt.show()