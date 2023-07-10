import math
import numpy as np 
import matplotlib.pyplot as plt
from numpy import random, mean, std, sqrt
#page60


#Define aceleration ar
#alpha = -8.4938e-05

n = 9000 #numero de iteraciones
dt = 0.01 #(input('pasos'))

x = np.zeros(n)
y = np.zeros(n)
Vx = np.zeros(n)
Vy = np.zeros(n)
V02 = (input('V02'))
rc = (input('rc'))
q = (input('q'))
x0 = (input('x0'))
y0 = (input('y0'))
Vx0 = (input('Vx0'))
Vy0 = (input('Vy0'))
X = np.array([x0, y0, Vx0, Vy0])


ti = n*dt #tiempo de integracion

def aceleration(x0, y0):

    a = (-V02)*np.array([x0/(rc**2 + (y0/q)**2 + x0**2), y0/((x0**2)*(q**2) + (rc**2)*(q**2) + y0**2)])    

    return a

def Xpunto(X):

    ac = aceleration(X[0], X[1])
    ar = np.array([X[2], X[3], ac[0], ac[1]])
    return ar


# Resolve ecuation dv/dt = a


 #RKN Calcula Posiciones y velocidades de manera paralela
def rKN(Xpunto, X,dt):
    k1 = Xpunto(X)*dt
    Xk = X + k1*0.5                              
    k2 = Xpunto(Xk)*dt
    Xk = X + k2*0.5
    k3 = Xpunto(Xk)*dt 
    Xk = X + k3
    k4 = Xpunto(Xk)*dt
    Xn = X+ (k1 + 2.*(k2 + k3) + k4)/6.
    return Xn


for i in range(n):
    x[i] = X[0]
    y[i] = X[1]
    Vx[i] = X[2]
    Vy[i] = X[3]
    X = rKN(Xpunto, X, dt)



#Calculate period with a counter

Xc = np.array([])
Yc = np.array([])
p = 10 #periodos

#j = 0
#while j<p:
#      xold = X[1]
#      X = rKN(Xpunto, X, dt)
#      if (xold*x[1]) and (x[3]>0):
#         p = p + 1
#         Xc = np.append(Xc, x[0])
#         Yc = np.append(Yc, x[2])

#Calculate Energy 
def Energy(Vx, Vy, x, y):
    En = 1/2.0 * (Vx**2 + Vy**2) + V02/2.0* (np.log(rc**2 + x**2 + (y/q)**2))
    return En


E = Energy(Vx, Vy, x, y)
E0 = 0.5666

t = np.arange(0, 10000)
#plt.plot(x, y)
#plt.show()   
plt.plot(t, E)
plt.show()
