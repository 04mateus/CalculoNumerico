# Cálculo numérico para engenharia elétrica com PYTHON
# Capítulo _8: Equações diferenciais parciais
# Diferênças Finitas no Domínio do Tempo


import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# Dimensões da grade em x (xdim) e y (ydim)
xdim=ydim= 100
xdim_dex = ydim_dex = xdim-1 # índices
# Número de passos de tempo
time_tot=350
# Posição da fonte
xsource= 50
ysource= 25
xsource_dex = xsource-1
ysource_dex = ysource-1
# Fator de estabilidade de Courant
S= 1/(2**0.5)
# Parâmetros de espaço livre
epsilon0 = (1/(36*pi))*1e-9
mu0 = 4*pi*(1e-7)
c = 3e+8
# Comprimento de passo na grade espacial
delta = 1e-6
# Passo da grade temporal obtido usando condição de Courant
deltat = S*(delta)/c
# Inicialização das matrizes de campo
Ez = np.zeros((xdim,ydim))
Hy = np.zeros((xdim,ydim))
Hx = np.zeros((xdim,ydim))
# Inicialização da permissividade e matrizes de permeabilidade
epsilon = np.dot((epsilon0),(np.ones((xdim,ydim))))
mu = mu0 * np.ones((xdim,ydim))
# Inicializando matrizes de condutividade elétrica e magnética
sigma = 4e-4*np.ones((xdim,ydim))
sigma_star = 4e-4*np.ones((xdim,ydim))
# Escolha da natureza da fonte
gaussian = 0
sine = 0
# O usuário pode dar a frequência de sua escolha para senoidal
frequency = 1.5e+13
impulse = 0
# Matrizes de fator multiplicativo para matriz H
A=((mu-0.5*np.dot(deltat, sigma_star))/(mu+0.5*np.dot(deltat, sigma_star)))
B=((deltat/delta)/(mu+0.5*np.dot(deltat, sigma_star)))
# Matrizes de fator multiplicativo para matriz E
C=((epsilon-0.5*np.dot(deltat, sigma))/(epsilon+0.5*np.dot(deltat, sigma)))
D=(deltat/delta)/(epsilon+0.5*np.dot(deltat, sigma))
# Loop de atualização começa
fig, ax = plt.subplots()
for n in range(0,time_tot,1):
  #if source is impulse or unit-time step
  if gaussian==0 and sine==0 and n==0:
    Ez[xsource_dex,ysource_dex]=1
  # Configurando barreiras dependentes do tempo
  if n<xsource-2:
    n1=xsource-n-1
  else:
    n1=1
  if n<xdim-1-xsource:
    n2=xsource+n
  else:
    n2=xdim-1
  if n<ysource-2:
    n11=ysource-n-1
  else:
    n11=1
  if n<ydim-1-ysource:
    n21=ysource+n
  else:
    n21=ydim-1
  # Atualização de vetores em vez de loops for para campos Hy e Hx
  n1 -= 1
  n2 -= 1
  n11 -= 1
  n21 -= 1
  Hy[n1:n2+1,n11:n21+1] = A[n1:n2+1, n11:n21+1]*Hy[n1:n2+1, n11:n21+1]+B[n1:n2+1,n11:n21+1]*(Ez[n1+1:n2+1+1,n11:n21+1]-Ez[n1:n2+1,n11:n21+1])
  Hx[n1:n2+1,n11:n21+1] = A[n1:n2+1, n11:n21+1]*Hx[n1:n2+1, n11:n21+1]-B[n1:n2+1,n11:n21+1]*(Ez[n1:n2+1,n11+1:n21+1+1]-Ez[n1:n2+1,n11:n21+1])
  # Atualização de vetor em vez de loop for para campo Ez
  Ez[n1+1:n2+1+1, n11+1:n21+1+1] = C[n1+1:n2+1+1, n11+1:n21+1+1]*Ez[n1+1:n2+1+1, n11+1:n21+1+1]+D[n1+1:n2+1+1, n11+1:n21+1+1]*(Hy[n1+1:n2+1+1, n11+1:n21+1+1]-Hy[n1:n2+1, n11+1:n21+1+1]-Hx[n1+1:n2+1+1, n11+1:n21+1+1]+Hx[n1+1:n2+1+1, n11:n21+1])
  # Condição de fronteira de condutor elétrico perfeito (CEP)
  Ez[0:xdim_dex+1, 0]=0
  Ez[0:xdim_dex+1, ydim_dex]=0
  Ez[0,  0:ydim_dex+1]=0
  Ez[xdim_dex, 0:ydim_dex+1]=0
  # Condições da fonte
  if impulse==0:
    # If unit-time step
    if gaussian==0 and sine==0:
      Ez[xsource_dex,ysource_dex]=1
    #Se senoidal
    if sine==1:
      tstart=1
      N_lambda=c/(frequency*delta)
      Ez[xsource_dex,ysource_dex]=np.sin(((2*pi*(c/(delta*N_lambda))*(n-tstart)*deltat)))
    #Se gaussiana
    if gaussian==1:
      if n<=42:
        Ez[xsource_dex,ysource_dex]=(10-5*np.cos(n*pi/20)+6*np.cos(2*n*pi/20)-np.cos(3*n*pi/20))/32
      else:
        Ez[xsource_dex,ysource_dex]=0
  else: #Se impulso
    Ez[xsource_dex,ysource_dex]=0
  #Visualização
  Ez_vis = np.transpose(Ez)
  Im = ax.imshow(Ez_vis, cmap = 'gist_heat', aspect='auto', vmax=1,vmin=-1) #cmap = 'autumn'; cmap = 'gist_rainbow'; cmap= 'seismic'. Link: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
  if n==0:
    cbar = fig.colorbar(Im,ticks=[-1,-0.5,0,0.5,1] )
    cbar.set_ticklabels(['-1','-0.5','0','0.5','1'])
  ax.set_title(f'Plotagem: imagem em escala de cor de Ez no domínio espacial com limite CEP. Tempo = {round(n*deltat*1e+15)} fs', fontweight="bold")
  ax.set_xlabel('x (in um)')
  ax.set_ylabel('y (in um)')
  plt.pause(0.1)
plt.show()