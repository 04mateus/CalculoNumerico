import numpy as np

# Funções que definem o sistema de equações não lineares
def f(T, Teq):
    eq1 = 10 + 0.5 * (T - Teq) * np.exp(-(T - Teq)) - 2 * (T - Teq)
    eq2 = 5 + 0.2 * (T - Teq) * np.exp(-(T - Teq)) - 0.8 * (T - Teq)
    return np.array([eq1, eq2])

# Derivadas parciais das funções em relação a T
def df(T, Teq):
    d_eq1 = 0.5 * np.exp(-(T - Teq)) - 0.5 * (T - Teq) * np.exp(-(T - Teq)) - 2
    d_eq2 = 0.2 * np.exp(-(T - Teq)) - 0.2 * (T - Teq) * np.exp(-(T - Teq)) - 0.8
    return np.array([d_eq1, d_eq2])

# Condições iniciais
T_guess = 50.0  # Suposição inicial para a temperatura
Teq_guess = 50.0  # Suposição inicial para a temperatura de equilíbrio

# Tolerância e número máximo de iterações
TOL = 1e-6
max_iter = 100

# Método de Newton-Raphson
for i in range(max_iter):
    F = f(T_guess, Teq_guess)
    J = df(T_guess, Teq_guess)
    delta = np.linalg.solve(J, -F)
    T_guess += delta[0]
    Teq_guess += delta[1]
    if np.linalg.norm(delta) < TOL:
        break

print(f"Temperatura de Equilíbrio: {Teq_guess:.4f}°C")
print(f"Temperatura no Ponto de Equilíbrio: {T_guess:.4f}°C")
