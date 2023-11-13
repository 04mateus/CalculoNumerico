import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parâmetros do circuito
R = 100.0  # Ohms
L = 0.5  # Henrys
C = 1e-6  # Farads
Vo = 20.0  # Volts

# Sistema de equações diferenciais
def circuito(y, t):
    i, v = y
    di_dt = v
    dv_dt = -R/L * v - i/(L*C)
    return [di_dt, dv_dt]

# Condições iniciais
i0 = 0.0
v0 = Vo
y0 = [i0, v0]

# Tempo de integração
tempo = np.linspace(0, 0.04, 10000)  # de 0 a 0.01 segundos

# Resolvendo as equações diferenciais
solucao = odeint(circuito, y0, tempo)

# Extraindo os resultados
corrente, tensao = solucao.T

# Encontrar o valor da corrente e o tempo correspondente
indice_pico_corrente = np.argmax(corrente)
valor_pico_corrente = corrente[indice_pico_corrente]
tempo_pico_corrente = tempo[indice_pico_corrente]

# Encontrar o tempo em que a tensão atinge o pico e não ultrapassa 0,5V
indice_pico_tensao = np.argmax(tensao)
tempo_pico_tensao = tempo[indice_pico_tensao]
tempo_0_5V = tempo[np.where(tensao < 0.5)[0][0]]

# Print dos resultados
print(f"Valor pico da corrente: {valor_pico_corrente:.4f} A em {tempo_pico_corrente:.4f} segundos.")
print(f"Tempo em que a tensão atinge o pico: {tempo_pico_tensao:.4f} segundos.")
print(f"Tempo em que a tensão não ultrapassa 0,5V: {tempo_0_5V:.4f} segundos.")

# Visualização dos resultados
plt.figure(figsize=(10, 6))

plt.subplot(211)
plt.plot(tempo, corrente, label='Corrente (A)')
plt.scatter(tempo_pico_corrente, valor_pico_corrente, color='red', marker='o', label='Pico de Corrente')
plt.title('Resposta do Circuito RLC')
plt.ylabel('Corrente (A)')
plt.grid(True)
plt.legend()

plt.subplot(212)
plt.plot(tempo, tensao, label='Tensão (V)', color='orange')
plt.scatter(tempo_pico_tensao, np.max(tensao), color='red', marker='o', label='Pico de Tensão')
plt.axhline(y=0.5, color='r', linestyle='--', label='Limite de 0,5V')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
