import math
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab

#from scipy.interpolate import interp1d(x, y, kind='linear', axis=-1, copy=True, bounds_error=True, fill_value=nan, assume_sorted=False)

from scipy.interpolate import interp1d
from MainProgram import*


#from PromedioMovil import*


#def InterpolateLightCurve(yp, ypnew):

#    return t

def fluxinterpolate(t,f):

    yin = (np.interp(f,t,f))

    plt.plot(t, f, 'o')
    plt.plot(t, yin, '--')
    plt.show()
    return n 

    

    return t, yin

yi = fluxinterpolate(t,f)
print len(yi)


