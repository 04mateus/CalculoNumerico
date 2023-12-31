# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 4: Raízes
# Método aberto: Newton-Raphson
# Diodo
# Adaptado de geeksforgeeks
# Referência: https://www.geeksforgeeks.org/program-for-newton-raphson-method/


import math as m
from scipy.misc import derivative
import numpy as np


def f(Id,  # Corrente no diodo (A)
      n=2,  # Coeficiente de emissão
      k=1.3806 * (10 ** (-23)),  # Constante de Boltzmann
      V=24,  # Tensão da fonte (V)
      T=300,  # Temperatura de operação (K)
      q=1.6022 * (10 ** (-19)),  # Carga do elétron
      Icr=31.9824 * (10 ** (-9)),  # Corrente de condução reversa (A)
      R=10):  # Resistência (Ohms)

    return (n * (k * T / q)) * m.log((Id / Icr) + 1, m.e) + R * Id - V


def d(x):
    return derivative(f, x)  # derivada função da SciPY


def newtonRaphson(x,  # x inicial
                  maxit=10,  # número máximo de iterações
                  TOL=0.0001):  # erro tolerado

    a = f(x) / d(x)
    iter = 0
    while abs(a) > TOL and iter < maxit:  # critério de parada
        a = f(x) / d(x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - a
        iter += 1
    return [x, iter]


# Exemplo
x0 = 2  # Valor inicial
ans = newtonRaphson(x0)
raiz = ans[0]
print(f'A raiz é {raiz:.5f}. Com {ans[1]} iterações.')