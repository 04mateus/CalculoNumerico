# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 4: Raízes
# Método intervalar: Bissecção
# Mateus Salgado

from math import cosh  # importa função logarítimo neperiano e a cte de euler

def f(C,  # comprimento do cabo (C)
        d = 500,  # distância entre as torres (d)
      f = 50): # flecha máxima permitida é permitida
    return C * (cosh(d/(2*C)) - 1) - f

def bisseccao(x1,  # x1 início do intervalo
              x2,  # x2 fim do intervalo
              TOL,  # erro tolerado
              iter=12):  # número máximo de iterações

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

resp = bisseccao(x1=500, x2=700, TOL=50, iter=10)
# print(resp)
print(f'raíz aprox {resp["hp"]:.4f}')
print(f'O número de iterações foi {resp["iteração"]}')