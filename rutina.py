from numpy import*
from math import* 
import matplotlib.pyplot as plt
from Spectrum import* 
from Vega import*
from Iconvolution import*




F0=Vega(Vega)
F=InterFlux(x1,xf,yf)


def magnitude(F0,F):
        m=[]
        m=-((2.5)*(log (F/F0)))
        return m

def colorg(magnitude):
    color=mag_aparente[0]-mag_aparente[1]
    return color
