import numpy as np
import math

#1 dimension
m1Array=[1,3]

def LightCurve(infile):
	measuremnts = open (infile,'r')
	xarray = []
	yarray = []
	for key2 in measuremnts:
		key2 = key2.replace('\n','')
		key2 = key2.replace("  "," ")
		key2 = key2.split(" ")
		x=xarray.append(float(key2[0]))
		y=yarray.append(float(key2[1]))
         
        infile = m1array

        return xarray
        for i in range(len(xArray)):
            print xarray[1]

#2dimension
#m2Array=[[1,2],[3,4]]

#for i in range(len(m2Array)):
 #   for j in range(len(m2Array[i])):
 #       print m2Array[i][j]
