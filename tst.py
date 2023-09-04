import numpy as np
from scipy.optimize import fsolve

# Parâmetros do circuito
f = 1e3  # Frequência (1 kHz)
L = 100e-3  # Indutância (100 mH)
R = 1e3  # Resistência (1 kΩ)

# Função da corrente Id
def current_equation(phi, beta):
    tan_phi = 2 * np.pi * f * L / R
    return np.sin(beta - phi) + np.sin(phi) * np.exp(-np.tan(phi)) - np.sin(beta)

# Encontrar o valor de beta para o qual a corrente se anula
def find_beta(phi):
    return fsolve(current_equation, phi, args=(phi,))[0]

# Valor inicial para o ângulo phi
initial_phi = np.pi / 4  # 45 graus em radianos

# Encontrar o valor de beta
beta_solution = find_beta(initial_phi)

# Converter o ângulo de radianos para graus
beta_degrees = np.degrees(beta_solution)

print(f"Ângulo β para o qual a corrente se anula: {beta_degrees:.4f} graus")
