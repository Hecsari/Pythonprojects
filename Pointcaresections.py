#Pointcare Sections
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt
E0 = 0.6 
Lz = 0.5
q = 0.6
V02 = 1
Rc = 0


#Energy
#E0 = 1/2 (x**2 + y**2) + Vo2/2*(ln[Rc**2 + x**2 + (y/q)**2])

x = np.arange(-10.0, 10.0, 0.01)

# #corte de Pointcare x1 = 0

def VelocityX(x, E0):

    Vx = np.sqrt(2*(E0 - (V02/2.0)*(np.log(Rc**2 + x**2))))

    return Vx

Vx = VelocityX(x, E0)


def VelocityY(x, E0, Vx):

    Vy = np.sqrt(2*(E0 - (V02/2.0)*(np.log(Rc**2 + x**2))) - Vx**2)

    return Vy

x0 = 0.5
y0 = 0
Vx0 = 1
Vy0 = 1.375

# #corte de Pointcare x2 = 0

def VelocityX2(x, E0):

    Vx2 = np.sqrt(2*(E0 - (V02/2.0)*(np.log(Rc**2 + x**2))))

    return Vx2

Vx2 = VelocityX2(x, E0)


def VelocityY2(x, E0, Vx):

    Vy2 = np.sqrt(2*(E0 - (V02/2.0)*(np.log(Rc**2 + x**2))) - Vx**2)

    return Vy2
#Vy = VelocityY(x0, E0, Vx0)

#print Vy
#plt.plot(x, Vx)
#plt.plot(x, -Vx)
#plt.xlim(-3.5, 3.5)
#plt.ylim(-3.5, 3.5)
plt.show()




    
