# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 5: Sistemas Lineares
# Método Direto: Decomposição LU
# Adaptado de cctmexico
# Referência: https://www.youtube.com/watch?v=FpVeXhAQg9w

import numpy as np


def LU_Decomposition_method(A, b):  # cria-se a função do método
    m = len(A)
    y = np.zeros(m)
    x = np.zeros(m)
    U = A
    L = np.zeros([m, m])
    for k in range(0, m):
        for r in range(0, m):
            if (k == r):
                L[k, r] = 1
            if (k < r):
                factor = (A[r, k]/A[k, k])
                L[r, k] = factor
                for c in range(0, m):
                    U[r, c] = A[r, c] - (factor * A[k, c])
    A = np.zeros([m, m])
    for r in range(0, m):
        for c in range(0, m):
            for k in range(0, m):
                A[r, c] += (L[r, k] * U[k, c])
    print('A')
    print(A)
    print('L')
    print(L)
    print()
    print('U')
    print(U)
    # RESOLUÇÃO DAS EQUAÇÕES MATRICIAIS
    ###################################
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    ###################################
    f = 'SOLUÇÃO DO SISTEMA'
    print('-'*(len(f)+32))
    print(f'{f:^50}')
    print('-'*(len(f)+32))
    print('x =')
    print(x)
    print('Onde: ')
    for c in range(0, len(x)):
        print(f'\t x[{c+1}] = {x[c]} \n')



# Uso do método
A = np.array([[1,1,1,2],
           [2,1,0,2],
           [0,1,1,1],
           [2,0,1,2]])
b = np.transpose([25, 25, 25, 15])
LU_Decomposition_method(A, b)