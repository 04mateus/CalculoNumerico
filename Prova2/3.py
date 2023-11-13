# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 9: Derivação numérica
# RL


from numpy import divide, diff
import matplotlib.pyplot as plt

t = ([0000, 0.2500, 0.5000, 0.7500, 1.0000, 1.2500, 1.5000])
P = ([1.0000, 0.9689,  0.8776,  0.7317, 0.5403,  0.3153, 0.0707])

t = ([0.0000, 0.2500, 0.5000, 0.7500, 1.0000])
I = ([0.9994,  0.9704,  0.8773, 0.7305,  0.5402])
L = 0.1
# V = L * d
d = divide(diff(I), diff(t))
tt = [0.0000, 0.1250, 0.3750, 0.6250, 0.8750]

print(f'd = {d}\n')
# print(f'V = {V}\n')

# Visualização
fig, ax = plt.subplots()
Corr = ax.plot(t, I, linewidth=1, marker='d', label='Corrente')
ax2 = ax.twinx()  # cria nova escala no lado oposto do gráfico eixo y
# Tens = ax2.plot(tt, V, linewidth=1, marker='s', label='Tensão', linestyle='--', color='k')
# lns = Tens + Corr
# labs = [l.get_label() for l in lns]
# ax.legend(lns, labs, loc=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax2.set_ylabel('Tensão (V)')
ax2.yaxis.grid(False)
plt.tight_layout()
plt.show()