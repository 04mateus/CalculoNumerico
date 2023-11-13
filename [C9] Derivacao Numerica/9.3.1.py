# Derivação numérica


#Importa a biblioteca necessária
from numpy import divide, diff
import matplotlib.pyplot as plt

#Parâmetros da questão
t = [0, 0.5, 1, 2, 3]
V = [100, 50, 35, 9.5, 0.05]
d = divide(diff(V), diff(t))
C = -0.01
I = C * d
tt = [0.25, 0.75, 1.5, 2.5]

#Imprime na tela resultado
print(f'd = {d}\n')
print(f'V = {V}\n')

#Visualização plotagem do gráfico
fig, ax = plt.subplots()
Corr = ax.plot(t, V, linewidth=1, marker='s', label='Tensão medida', linestyle='--', color='k')
ax2 = ax.twinx()  # cria nova escala no lado oposto do gráfico eixo y
Tens = ax2.plot(tt, I, linewidth=1, marker='d', label='Corrente estimada')
lns = Tens + Corr
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Tensão (V)')
ax2.set_ylabel('Corrente (A)')
ax2.yaxis.grid(False)
plt.tight_layout()
plt.show()