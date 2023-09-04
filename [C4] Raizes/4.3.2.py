# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 4: Raízes
# Método intervalar: Bissecção

import math as m
from math import *  # importa função logarítimo neperiano e a cte de euler
from scipy.misc import derivative


def f(B,
      id = 0,
      f=1000,
      L = 0.1,
      R = 1000):
    tanfi = 2*m.pi*f*L/R
    # print(tanfi)
    fi = m.atan(tanfi)
    # print(fi)
    fi = m.degrees(fi)
    # print(fi)

    return m.sin(m.radians(B-fi))+(m.sin(m.degrees(fi))*m.exp(-B/tanfi))


def bisseccao(x1,  # x1 início do intervalo
              x2,  # x2 fim do intervalo
              TOL,  # erro tolerado
              iter=30):  # número máximo de iterações

    hp = (x1 + x2)/2  # Ponto médio entre os valores x1 e x2
    if f(x1) * f(x2) > 0:
        print("Nenhuma raíz encontrada.")  # nenhuma raíz.
    else:
        c = 0  # variável contador
        ERRO = abs(f(x2) - f(x1))  # diferença entre os valores de y
        while ERRO > TOL or c < iter:  # loop iterativo com critérios de parada
            hp = (x1 + x2) / 2.0
            if f(hp) == 0:
                return [hp, c]
            elif f(x1) * f(hp) < 0:
                x2 = hp
                c += 1  # contagem
            else:
                x1 = hp
            ERRO = abs(f(x2) - f(x1))
        return {"hp": hp, "iteração": c}  # raíz da função; número de iterações

resp = bisseccao(x1=200, x2=250, TOL=5, iter=10)
# print(resp)
print(f'raíz aprox {resp["hp"]:.4f}')
print(f'O número de iterações foi {resp["iteração"]}')