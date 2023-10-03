import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab
import sys
from numpy import random, mean, std, sqrt
#def flux2mag(xarray, yarray):

infile = '757450.dat'

def LightCurve(infile):
        #This read and convert to arreglos of the data
	measuremnts = open (infile,'r')
	xarray = []
	yarray = []
	for key2 in measuremnts:
		key2 = key2.replace('\n','')
		key2 = key2.replace("  "," ")
		key2 = key2.replace("  "," ")
		key2 = key2.replace("  "," ")
		key2 = key2.replace("  "," ")
		key2 = key2.replace("  "," ")
		key2 = key2.replace("  "," ")
		key2 = key2.split(" ")
		xarray.append(float(key2[0]))
		yarray.append(float(key2[1]))       

           #This all is for create and save a figure with the values of data
	f= plt.figure(figsize=(15,5))	
	mpl.rcParams['axes.linewidth'] = 2.
	ax = f.add_subplot(121)
	ax.set_position([0.15,0.15,0.80,0.80])
	pylab.yticks(size = 15,rotation = 0)
	pylab.xticks(size = 15,rotation = 0)
	plt.ylim(0., np.max(yarray))
	plt.xlim(0., np.max(xarray))
	plt.xlabel("Time(BJD-2454883)", size = 20)
	plt.ylabel("PDCSAP-Flux(e/s)", size = 20)
	
	ax.plot(xarray,yarray,'-',color = 'Blue',markersize=20,lw=1.5,alpha=0.5)

	f.savefig('Figure'+infile+'.png')
        return xarray, yarray
       
t, f = LightCurve(infile)   #save the values
print t[0], f[0]    #print the first elements of the data


 


       






