# Sistemas Não Lineares
# Metodo: Newton Raphson
# Questão: 1
# Fellipe Carvalho


from math import pi, exp
from numpy import array, divide, linalg

Icr = 31.9824 * 10 ** (-9)
n = 2
k = 1.3806 * 10 ** (-23)
T = 300
q = 1.6022 * 10 ** (19)
V = 24
R = 10

x = array([[1], [2]])
iter = 0
maxit = 50
es = 0.001
while True:
    f1 = (Icr((exp ** (x(2) / (n * k * T / q) - 1)))) - x(1)
    f2 = ((V - x(2)) / R) - x(1)
    F = array([f1, f2])  # Matriz de funções

    J = array([[-1, Icr * (exp ** (x(2) / (n * k * T / q)) - 1) / (n * k * T / q)],
               [-1, -1 / R]])  # Matriz Jacobiana
    dx = linalg.lstsq(J, F, rcond=None)[0]
    x = x - dx
    iter += 1
    ea = max(abs(divide(dx, x)))
    if iter >= maxit or ea <= es:
        break
print(f'Com {iter} iterações: \n x = \n {x}')