import math
import numpy as np 
from matplotlib.pylab import*
from numpy import random, mean, std, sqrt
#page60


rp = 1
m = 1
#Define aceleration ar
dt = 0.2 #paso de tiempo
n = 2500 #numero de iteraciones
#(input('pasos'))
ti = n*dt #tiempo de integracion
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

g = 1
m = 1
p = 0
for i in range(n):
    x[i] = X[0]
    y[i] = X[1]
    Vx[i] = X[2]
    Vy[i] = X[3]
    V = np.array([Vx, Vy])
    X = rKN(Xpunto, X, dt)
   # if X[0]*x[i] < 0:
   #    p = p + 1 
    En = (0.5)*m*(Vx**2 + Vy**2) + (V02*0.5)
#*(np.log(rc**2 + x**2 + (y/q)**2))
   


#Calculate period



    
plot(x, y)
show()   

