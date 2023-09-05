import math

def f(x):
    return x**2 - 4*x + 2

def df(x):
    return 2*x - 4

def newtonRaphson(x0, maxit=10, TOL=0.0001):
    iter = 0
    while iter < maxit:
        a = f(x0) / df(x0)
        x1 = x0 - a
        erro_relativo = abs((x1 - x0) / x1)



        print(f'Iteração {iter}:  x1 = {x1}, x = {x0}, Erro Relativo = {(erro_relativo)/100:.5f}')
        x0 = x1
        iter += 1
        if erro_relativo > TOL:
            break

    return [x0, iter]

# Exemplo
x0 = 3  # Valor inicial
ans = newtonRaphson(x0)
raiz = ans[0]
print(f'A raiz é {raiz:.5f}. Com {ans[1]} iterações.')
