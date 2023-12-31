# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo _8: equações diferenciais parciais
# Modelagem por linhas de transmissão
## Modelagem por linha de transmissão série 2D implementação PYTHON para guia de onda


import cmath as cm
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3d
## Características do meio
co = 3e+8
Eps0 = 8.85 * 1E-12
pi = np.pi
Mu0 = 4 * pi * 1E-7
velocidade = 1 / np.sqrt(Eps0 * Mu0)
Z0 = 120 * pi  # Impedancia do espaço livre
Ztl = Z0 / np.sqrt(2)
## Dimensões física do guia de onda e modos de propagação
a = 19.05E-3
b = 9.525E-3
c = 52  # Número de pontos no eixo x (+ 2 colunas)
l = 27  # Número de pontos no eixo y (+ 2 linhas)
#### Dimensões maiores para não zerar indíces de i-1=0
deltal = 0.381e-3  # Distancia entre os nós)
deltat = 0.898e-12
## Modo de propagação
m = 1
n = 0
fc = (co / (2 * pi)) * np.sqrt((((m * pi) / a) ** 2) + (((n * pi) / b) ** 2))  # Frequência de corte
lambdac = co / fc
cj = complex(0, 1)
T = (1 / fc)  # período de oscilação de cada modo
Tk = round((T / 2) / deltat)  # T/2 correspondente ao número de interações
## Inicialização dos vetores e matrizes
ninter = 3000  # Número de interações
ttotal = ninter * deltat  # Tempo total de simulação
pg = np.zeros(ninter)  # Vetor Pulso Gaussiano/Interações
mvi= np.zeros((l, c, 4, ninter),dtype = 'complex_')   # Matriz de Vis todos pontos repetida 4x (4portas)
mvr =np.zeros((l, c, 4, ninter),dtype = 'complex_')  # Matriz de Vrs todos pontos repetida 4x (4portas)
Ex = np.zeros((l, c, ninter),dtype = 'complex_')  # Matriz de Ex para todos os pontos
Ey = np.zeros((l, c, ninter),dtype = 'complex_')   # Matriz de Ey para todos os pontos
Hz = np.zeros((l, c, ninter),dtype = 'complex_')   # Matriz de Hz para todos os pontos
Hzs = np.zeros(ninter,dtype = 'complex_')   # Vetor com valores de Hz (ponto específico)
Exs = np.zeros(ninter,dtype = 'complex_')   # Vetor com valores de Ex (ponto específico)
Eys = np.zeros(ninter,dtype = 'complex_')   # Vetor com valores de Ey (ponto específico)
fEy = np.zeros((l, c, ninter),dtype = 'complex_')
fHz = np.zeros((l, c, ninter),dtype = 'complex_')
fftHzs = np.zeros(ninter,dtype = 'complex_')
fftEys = np.zeros(ninter,dtype = 'complex_')
## Formatação do Pulso Gausiano
Eo = 1  # Amplitude do pulso
D = 10 * deltat  # Duração do pulso
L = 10 * deltat  # Largura do pulso
# pg=Eo*(exp(-18*((t-D)/L)**2))
## Início da interação no tempo (loop principal)
for k in range(0,ninter):
    t = deltat * k
    pg[k] = ((Eo * (np.exp(-18 * (((t - D) / L) ** 2)))) * ((0.5 * deltal)))  # Valores de V2=V4
    # Excitação (Sobrescreve os valores de tensão pulso enquanto ele existir)
    if k <= 19:
        mvi[1: 27, 25, 1, k]= - pg[k]
        mvi[1: 27, 25, 3, k]= - pg[k]
        mvi[1: 27, 25, 0, k]= 0
        mvi[1: 27, 25, 2, k]= 0
    ## Início de inteações de linhas e colunas
    for i in range(1,l - 1):
        for j in range(1,c - 1):
            #### Cálculo dos campos
            Ex[i, j, k] = -((mvi[i, j, 0, k] + mvi[i, j, 2, k]) / deltal)
            Ey[i, j, k] = -((mvi[i, j, 1, k] + mvi[i, j, 3, k]) / deltal)
            Hz[i, j, k] = ((mvi[i, j, 0, k] + mvi[i, j, 3, k] - mvi[i, j, 2, k] - mvi[i, j, 1, k]) / (2 * Ztl)) / deltal
            ## DTF para todos os pontos da malha para uma frequência de corte
            if k > 1:
                fEy[i, j, k] = fEy[i, j, k - 1] + Ey[i, j, k] * cm.exp(-2 * cj * pi * fc * t)
                fHz[i, j, k] = fHz[i, j, k - 1] + Hz[i, j, k] * cm.exp(-2 * cj * pi * fc * t)
            else:
                fEy[i, j, k] = Ey[i, j, k] * cm.exp(-2 * cj * cm.pi * fc * t)
                fHz[i, j, k] = Hz[i, j, k] * cm.exp(-2 * cj * cm.pi * fc * t)
            ## Matriz Vs refletidas no mesmo K
            mvr[i, j, 0, k] = 0.5 * (mvi[i, j, 0, k] + mvi[i, j, 1, k] + mvi[i, j, 2, k] - mvi[i, j, 3, k])
            mvr[i, j, 1, k] = 0.5 * (mvi[i, j, 0, k] + mvi[i, j, 1, k] - mvi[i, j, 2, k] + mvi[i, j, 3, k])
            mvr[i, j, 2, k] = 0.5 * (mvi[i, j, 0, k] - mvi[i, j, 1, k] + mvi[i, j, 2, k] + mvi[i, j, 3, k])
            mvr[i, j, 3, k] = 0.5 * (-mvi[i, j, 0, k] + mvi[i, j, 1, k] + mvi[i, j, 2, k] + mvi[i, j, 3, k])
            if k != 2999:
              ## Conexão com nó seguinte
              mvi[i + 1, j, 2, k + 1] = mvr[i, j, 0, k]
              mvi[i - 1, j, 0, k + 1] = mvr[i, j, 2, k]
              mvi[i, j - 1, 3, k + 1] = mvr[i, j, 1, k]
              mvi[i, j + 1, 1, k + 1] = mvr[i, j, 3, k]
              ## Condição de contorno
              mvi[25,:, 0, k + 1]=-mvr[25,:, 0, k]
              mvi[1,:, 2, k + 1]=-mvr[1,:, 2, k]
              mvi[:, 1, 1, k + 1]=-mvr[:, 1, 1, k]
              mvi[:, 50, 3, k + 1]=-mvr[:, 50, 3, k]
    # Saídas para um ponto específico da malha
    Hzs[k] = Hz[12, 28, k]
    Exs[k] = Ex[12, 28, k]
    Eys[k] = Ey[12, 28, k]
    print(f'{(ninter-k-1)} iterações restantes')
vetorf = np.linspace(0, 30, 3000)
vetort = np.arange(0, ninter-1,1) * deltat
# Visualização
plt.rcParams["figure.frameon"] = False
plt.rcParams['figure.constrained_layout.use'] = True
fig, (ax1, ax2)= plt.subplots(nrows = 1, ncols = 2, constrained_layout=True, frameon = False)
# figura(1)
X1, Y1 = np.meshgrid( np.arange(51),np.arange(25))
Z1= np.abs(fEy[1:26,1:52,1499])
ax1 = fig.add_subplot(121, projection='3d')
h1 = ax1.plot_surface(X1,Y1,Z1, cmap = 'jet', edgecolor='k')
ax1.set_xlabel('Nx')
ax1.set_ylabel('Ny')
ax1.set_zlabel('fEy')
# figura(2)
X2, Y2 = np.meshgrid( np.arange(50),np.arange(25))
Z2= np.abs(fHz[1:26,1:51,1499] )
ax2 = fig.add_subplot(122, projection='3d')
h2 = ax2.plot_surface(X2,Y2,Z2, cmap = 'jet', edgecolor='k')
ax2.set_xlabel('Nx')
ax2.set_ylabel('Ny')
ax2.set_zlabel('fHz')
plt.show()