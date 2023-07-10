import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import numpy as np
import sys
from numpy import random, mean, std, sqrt
#import MainProgram
from MainProgram import*


#IMPORTANT:Check the graphs of normalizationcurve

def normalizationflux(f):
    m = []
    m1 = mean(f[0:1624])    #saca el promedio de cada pedazo
    m2 = mean(f[1624:5694])
    m3 = mean(f[5694:9776])
    m4 = mean(f[9776:18421])
    m5 = mean(f[18421:22693])
    m6 = mean(f[22693:26919])
    m7 = mean(f[26919:210715])
    m8 = mean(f[210715:370376])
    m9 = mean(f[370376:568066])
    m10 = mean(f[568066:696984])
    m11 = mean(f[696984:828584])
  
    m = ( m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11)


    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    n8 = []
    n9 = []
    n10  = []
    n11  = []
    
    
    n1 = ([j - m1  for j in f[0:1624] ])    #normaliza el flujo para cada pedazo
    n2 = ([j - m2  for j in f[1624:5694] ])
    n3 = ([j - m3  for j in f[5694:9776] ])
    n4 = ([j - m4  for j in f[9776:18422] ])
    n5 = ([j - m5  for j in f[18422:22693] ])
    n6 = ([j - m6  for j in f[22693:34635] ])
    n7 = ([j - m7  for j in f[34635:210715] ])
    n8 = ([j - m8  for j in f[210715:370376] ])
    n9 = ([j - m9  for j in f[370376:568066] ])
    n10 = ([j - m10 for j in f[568066:696984] ])
    n11 = ([j - m11 for j in f[696984:828584] ])

    n = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11) #junta todos los valores en un solo arreglo

    f= plt.figure(figsize=(15,5))	#Size of the figure
    mpl.rcParams['axes.linewidth'] = 2.
    ax = f.add_subplot(121)
    ax.set_position([0.15,0.15,0.80,0.80])   #Position of the figure
    pylab.yticks(size = 15,rotation = 0)
    pylab.xticks(size = 15,rotation = 0)
    plt.ylim(-1500, 1500)                  #y axe limit
    plt.xlim(130.0, 1500.0)                  #x axe limit
    plt.xlabel("Time(BJD-2454883)", size = 20)  #Title of x label
    plt.ylabel("PDCSAP-Flux(e/s)", size = 20)   #Title of y label
    ax.plot(t,n,'-',color = 'Blue',markersize=20,lw=1.5,alpha=0.5)
    f.savefig('Normalization'+infile+'.png')  #Save figure
    return n 

yn = normalizationflux(f) 






   




    



