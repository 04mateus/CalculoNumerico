# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 6: Sistemas Não Lineares
# Método iterativo: Newton-Raphson
# Circuito magnético


from math import pi, exp
from numpy import array, divide, linalg

lf = 0.4  # comprimento médio no ferro (m)
le = 0.0008  # comprimento médio no entreferro (m)
N = 200  # Número de espiras
I = 10  # Corrente elétrica(A)
mi = 4 * pi * 10 ** (-7)
x = array([[1250000],  # aproximações iniciais
           [70]])
iter = 0
maxit = 50
es = 0.001
while True:
    f1 = (2 * x[0] * le + x[1] * lf - N * I)
    f2 = (-mi * x[0] + 1.8 * (1 - exp(-(x[1]) / 40)))
    F = array([f1, f2])  # Matriz de funções

    J = array([[2 * le, lf],
               [-mi, 1.8 * (1 / 40) * exp(-(x[1]) / 40)]])  # Matriz Jacobiana
    dx = linalg.lstsq(J, F, rcond=None)[0]
    x = x - dx
    iter += 1
    ea = max(abs(divide(dx, x)))
    if iter >= maxit or ea <= es:
        break
print(f'Com {iter} iterações: \n x = \n {x}')