# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 4: Raízes
# Método intervalar: Bissecção
# Diodo

from math import log, e  # importa função logarítimo neperiano e a cte de euler

def f(Id,  # Corrente no diodo (A)
        n=2,  # Coeficiente de emissão
        k=1.3806 * (10 ** (-23)),  # Constante de Boltzmann
        V=24,  # Tensão da fonte (V)
        T=300,  # Temperatura de operação (K)
        q=1.6022 * (10 ** (-19)),  # Carga do elétron
        Icr=31.9824 * (10 ** (-9)),  # Corrente de condução reversa (A)
        R=10):  # Resistência (Ohms)

    return (n * (k * T / q)) * log((Id / Icr) + 1, e) + R * Id - V

def bisseccao(x1,  # x1 início do intervalo
              x2,  # x2 fim do intervalo
              TOL,  # erro tolerado
              iter=16):  # número máximo de iterações

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

resp = bisseccao(x1=2, x2=2.5, TOL=0.0001, iter=16)
print(f'raíz aprox {resp["hp"]:.4f}')
print(f'O número de iterações foi {resp["iteração"]}')