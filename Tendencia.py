import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import sys
from scipy import stats
from Normalization import*

#x = [1,2,3,4,5,6]
#y = [2,4,6,8,10,12]

def LinearRegressionLC(t,yi):

    slope, intercept, r_value, p_value, std_err = stats.linregress(t,yi)  #Function for obtain the slope of the linear regression
    # To get coefficient of determination (r_squared)                     
    return slope, intercept, r_value, p_value, std_err

sl, inter, r_v, p_v, std = LinearRegressionLC(t,yi)
 
#print sl #muestra el valor de la pendiente


def FluxTrend(sl):
    ynt = []
    ynt = ([i - sl for i in yi])   #Eliminate trends

    f= plt.figure(figsize=(15,5))	#Size of the figure
    mpl.rcParams['axes.linewidth'] = 2.
    ax = f.add_subplot(121)
    ax.set_position([0.15,0.15,0.80,0.80])   #Position of the figure
    pylab.yticks(size = 15,rotation = 0)
    pylab.xticks(size = 15,rotation = 0)
    plt.ylim(-1500.0, -1500.0)                  #y axe limit
    plt.xlim(130.0, 1500.0)                  #x axe limit
    plt.xlabel("Time(BJD-2454883)", size = 20)  #Title of x label
    plt.ylabel("PDCSAP-Flux(e/s)", size = 20)   #Title of y label
    ax.plot(t,ynt,'-',color = 'Blue',markersize=20,lw=1.5,alpha=0.5)
    f.savefig('Tendencia'+infile+'.png')  #Save figure
    return ynt

yt = FluxTrend(sl) 
#print  yt







#REALIZAR UN AJUSTE LINEAL

#SACAR LA PENDIENTE Y GUARDARLA EN UNA VARIABLE

#RESTARLE LA PENDIENTE A LOS DATOS




#    return 

   

 #  = Tendencia ()



