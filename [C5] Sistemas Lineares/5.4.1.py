# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 5: Sistemas Lineares
# Métodos Diretos: Eliminação de Gauss
# Referência: https://www.youtube.com/watch?v=ZDxONtacA_4&t=1310s
# Mateus Salgado


from numpy import array, zeros


def GaussEliminação(A, b):  # cria-se função do método
    n = len(b)
    x = zeros(n, float)
    # Eliminação progressiva
    for k in range(n-1):
        for i in range(k+1, n):
            if A[i, k] == 0:
                continue
            fator = A[k, k] / A[i, k]
            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j]*fator
            b[i] = b[k] - b[i]*fator
    print(f'A =\n {A}')
    print(f'b =\n {b}')
    # Substituição regressiva
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += A[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / A[i, i]
    f = 'SOLUÇÃO DO SISTEMA'
    print('-'*(len(f)+32))
    print(f'{f:^50}')
    print('-'*(len(f)+32))
    print(x)
    print('Onde: ')
    r3 = 0
    for c in range(0, len(x)):
        print(f'\t x[{c}] = {x[c]} \n')
        r3 += x[c]


    print('A soma dos dois valores é igual ao valor de R3 ')
    print(f'R3 = {r3}')

# Uso do método
A = array([[20,10],
          [10,20]])
b = array([100, 100])

GaussEliminação(A, b)