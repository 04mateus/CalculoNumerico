import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Função que retorna a derivada da EDO
def modelo(T, t, k, T_ambiente):
    dTdt = -k * (T - T_ambiente)
    return dTdt

# Condições iniciais
T0 = 100.0        # Temperatura inicial do objeto em graus Celsius
T_ambiente = 25.0 # Temperatura ambiente em graus Celsius
k = 0.1           # Constante de resfriamento

# Tempo
tempo = np.linspace(0, 60, 100) # de 0 a 60 minutos, com 100 pontos intermediários

# Resolve a EDO numericamente
solucao = odeint(modelo, T0, tempo, args=(k, T_ambiente))

# Calcula a derivada da temperatura em relação ao tempo
derivada_temperatura = -k * (solucao[:, 0] - T_ambiente)

# Encontra o momento de maior derivada
indice_max_derivada = np.argmax(np.abs(derivada_temperatura))
momento_max_derivada = tempo[indice_max_derivada]
valor_max_derivada = derivada_temperatura[indice_max_derivada]

# Plota o resultado
plt.plot(tempo, solucao[:, 0], label='Temperatura do objeto')
plt.axhline(y=T_ambiente, color='r', linestyle='--', label='Temperatura ambiente')
plt.scatter(momento_max_derivada, solucao[indice_max_derivada, 0], color='g', label='Maior derivada')
plt.title('Resfriamento de um objeto')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.show()

print(f'O momento de maior derivada ocorre em t = {momento_max_derivada:.2f} minutos.')
print(f'O valor da maior derivada é {valor_max_derivada:.2f} °C/minuto.')
