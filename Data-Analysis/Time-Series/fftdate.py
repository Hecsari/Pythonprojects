import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import sys
from scipy.fftpack import fft, ifft
from PromedioMovil import*



def FFTLightCurve(yp):
    yfft = []
    yfft.append(fft(yp))


    f= plt.figure(figsize=(15,5))	#Size of the figure
    mpl.rcParams['axes.linewidth'] = 2.
    ax = f.add_subplot(121)
    ax.set_position([0.15,0.15,0.80,0.80])   #Position of the figure
    pylab.yticks(size = 15,rotation = 0)
    pylab.xticks(size = 15,rotation = 0)
    plt.ylim(0.0, 1500.0)                  #y axe limit
    plt.xlim(0.0, 1500.0)                  #x axe limit
    plt.xlabel("Time(BJD-2454883)", size = 20)  #Title of x label
    plt.ylabel("PDCSAP-Flux(e/s)", size = 20)   #Title of y label
    ax.plot(t,yfft,'-',color = 'Blue',markersize=20,lw=1.5,alpha=0.5)
    f.savefig('FastFourierTransform'+infile+'.png')  #Save figure

    return yfft

yff = FFTLightCurve(yp)
print "Fast Fourier Transform is", yff


#def IFFTLightCurve(yf):
 #   yinv = ifft(yf)
 #   return yinv

#yif = IFFTLightCurve(yf)
#print "Inverse Fast Transform Fourier is", yif

     #Graph of the FFT and IFFT




#information about fft: https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html, https://docs.scipy.org/doc/numpy/reference/routines.fft.html, https://docs.scipy.org/doc/scipy-0.18.1/reference/tutorial/fftpack.html 
