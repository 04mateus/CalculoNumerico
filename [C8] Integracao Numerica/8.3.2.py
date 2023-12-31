# Integração numérica

# Biblioteca necessária
import numpy as np
import matplotlib.pyplot as plt


# definição das variáveis
def feval(Nomefuncao, *argumentos):
    return eval(Nomefuncao)(*argumentos)


t = [0, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00]
P = [100, 36.90, 13.50, 5.06, 1.99, 0.62, 0.25]

plt.plot(t, P, 'o', markerfacecolor='none', markeredgecolor='r')

m = 6
c = np.polyfit(t, P, m)  # ajusta por mínimos quadrados um polinômio de n grau
xx = np.linspace(t[0], t[-1], 100)  # numero de pontos para polinômio de grau maior
yy = np.polyval(c, xx)
plt.plot(xx, yy, 'r-')

# c =   [0.5582,   -6.6480,   34.2689, -100.5233,  181.5979, -195.7537,  100.0000]

x = xx
ff = 0.5582 * x ** 6 - 6.6480 * x ** 5 + 34.2689 * x ** 4 - 100.5233 * x ** 3 + 181.5979 * x ** 2 - 195.7537 * x + 100.0000
plt.plot(x, ff, 'k-')
plt.xlabel('t (s)')
plt.ylabel('P(t) (W)')

a = 1
b = 2

tit = f'POTENCIA MÉDIA NO INTERVALO ENTRE {a} E {b} s'
# Imprime na tela resultados
print('\t', '-' * len(tit))
print(f'\t {tit}')
print('\t', '-' * len(tit), '\n')
# trapezio
n = 100

x = np.linspace(a, b, n)
ff = 0.5582 * x ** 6 - 6.6480 * x ** 5 + 34.2689 * x ** 4 - 100.5233 * x ** 3 + 181.5979 * x ** 2 - 195.7537 * x + 100.0000
Int = np.trapz(ff, x)
Pmed = (1 / (b - a)) * Int

print(f'Por trapézio, com n = {n}, Pmed = {Pmed:.4f}.\n')


# Quadratura adaptativa


def quadsetp(f, a, b, tol, fa, fc, fb):
    h = b - a
    c = (a + b) / 2
    fd = feval('f', (a + c) / 2)
    fe = feval('f', (c + b) / 2)
    q1 = h / 6 * (fa + 4 * fc + fb)
    q2 = h / 12 * (fa + 4 * fd + 2 * fc + 4 * fe + fb)
    i = 1
    if abs(q2 - q1) <= tol:
        q = q2 + (q2 - q1) / 15
    else:
        qa = quadsetp(f, a, c, tol, fa, fd, fc)
        qb = quadsetp(f, c, b, tol, fc, fe, fb)
        q = qa + qb
    return q


f = lambda \
    x: 0.5582 * x ** 6 - 6.6480 * x ** 5 + 34.2689 * x ** 4 - 100.5233 * x ** 3 + 181.5979 * x ** 2 - 195.7537 * x + 100.0000

c = (a + b) / 2
fa = feval('f', a)
fb = feval('f', b)
fc = feval('f', c)
tol = 1 * np.exp(-.01)

q = quadsetp(f, a, b, tol, fa, fc, fb)

Int = q
Pmed = (1 / (b - a)) * Int

print(f'Por quadratura adaptativa, com 1 ação recursiva, Pmed = {Pmed:.4f}.\n')
plt.ylim(0, max(yy))
plt.hlines(xmin=a, xmax=b, y=Pmed, label='Pmed', color='blue')
plt.vlines(ymax=feval('f', a), ymin=0, x=a, linestyles='dashed')
plt.vlines(ymax=Pmed, ymin=0, x=b, linestyles='dashed')
plt.tight_layout()
plt.legend()
plt.show()