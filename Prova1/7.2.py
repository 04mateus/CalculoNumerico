# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 6: Sistemas Não Lineares
# Método iterativo: Newton-Raphson
# Circuito magnético


from math import pi, exp
from numpy import array, divide, linalg

x = array([5,  # aproximações iniciais
           5])
iter = 0
maxit = 50
es = 0.001
while True:
    f1 = 10 * x[0] + 10 * x[0] * x[1] - 50
    f2 = 10 * x[1] + 10 * x[0] * x[1] - 50
    F = array([f1, f2])  # Matriz de funções

    J = array([[10 + 10 * x[1], 10 * x[0]],
               [10 * x[1], 10 + 10 * x[0]]])  # Matriz Jacobiana

    dx = linalg.lstsq(J, F, rcond=None)[0]
    x = x - dx
    iter += 1
    ea = max(abs(divide(dx, x)))

    # print(f'inter{iter}')
    # print(f'x{x}')
    # print(f'err{ea/100}')

    if iter >= maxit or ea <= es:
        break
print(f'Com {iter} iterações: \n x = \n {x}')