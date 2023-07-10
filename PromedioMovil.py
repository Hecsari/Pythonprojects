import math
import numpy as np
import pylab
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from Tendencia import*


def rollingmeanflux(yt):
    data = {'score': yt}
    df = pd.DataFrame(data)
    pm  = pd.rolling_mean(df, 10)

    f= plt.figure(figsize=(15,5))	#Size of the figure
    mpl.rcParams['axes.linewidth'] = 2.
    ax = f.add_subplot(121)
    ax.set_position([0.15,0.15,0.80,0.80])   #Position of the figure
    pylab.yticks(size = 15,rotation = 0)
    pylab.xticks(size = 15,rotation = 0)
    plt.ylim(-1500.0, 1500.0)                  #y axe limit
    plt.xlim(130.0, 1500.0)                  #x axe limit
    plt.xlabel("Time(BJD-2454883)", size = 20)  #Title of x label
    plt.ylabel("PDCSAP-Flux(e/s)", size = 20)   #Title of y label
    ax.plot(t,pm,'-',color = 'Blue',markersize=20,lw=1.5,alpha=0.5)
    f.savefig('Rollingmeanpm'+infile+'.png')  #Save figure


    return pm


yp = rollingmeanflux (yt)





#d_mva = PD.rolling_mean(D, 10)

