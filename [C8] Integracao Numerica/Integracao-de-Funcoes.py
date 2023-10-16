# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo 8: Integração numérica
# Quadratura Adaptativa
# Referência: https://bytes.com/topic/python/answers/29829-feval-similar-matlab


import numpy as np


def feval(Nomefuncao, *argumentos):
    return eval(Nomefuncao)(*argumentos)


def f(x):
    return (10 * np.exp(np.divide(-x, 0.001))) ** 2


def quadsetp(f, a, b, tol, fa, fc, fb):
    h = b - a
    c = (a + b) / 2
    fd = feval('f', (a + c) / 2)
    fe = feval('f', (c + b) / 2)
    q1 = h / 6 * (fa + 4 * fc + fb)
    q2 = h / 12 * (fa + 4 * fd + 2 * fc + 4 * fe + fb)
    if abs(q2 - q1) <= tol:
        q = q2 + (q2 - q1)/15
    else:
        qa = quadsetp(f, a, c, tol, fa, fd, fc)
        qb = quadsetp(f, c, b, tol, fc, fe, fb)
        q = qa + qb
    return q


a = 0
b = 0.003
c = (a+b) / 2
tol = 1 * np.exp(-6)
fa = feval('f', a)
fb = feval('f', b)
fc = feval('f', c)
w = quadsetp(f, a, b, tol, fa, fc, fb)
print(f'w = {w}')