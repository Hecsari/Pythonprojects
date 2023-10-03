import pandas as pd
import scipy 
import numpy as np
import astropy
import matplotlib.pyplot as plt
from astropy.table import Table

ap=pd.read_csv('start.csv', delimiter=',')

ap['l']=ap.GLON*np.pi/180
ap['b']=ap.GLAT*np.pi/180
ap['ra']=ap.RA*np.pi/180
ap['dec']=ap.DEC*np.pi/180

ap['d']=1000/ap.plx
ap['X']=8300-ap.d*np.cos(ap.b)*np.cos(ap.l)
ap['Y']=ap.d*np.cos(ap.b)*np.sin(ap.l)
ap['Z']=ap.d*np.sin(ap.b)
ap['C1']=(np.sin(0.4734772828)*np.cos(ap.dec))-(np.cos(0.4734772828)*np.sin(ap.dec)*np.cos(ap.ra-3.36603291968))
ap['C2']=np.cos(0.4734772828)*np.sin(ap.ra-3.36603291968)
ap['C']=np.sqrt(ap.C1*ap.C1+ap.C2*ap.C2)
ap['pml']=((ap.C1/ap.C)*ap.pmra*np.cos(ap.dec)+(ap.C2/ap.C)*ap.pmdec)/np.cos(ap.dec)
ap['pmb']=(ap.C1/ap.C)*ap.pmdec-(ap.C2/ap.C)*ap.pmra*np.cos(ap.dec)
ap['Vl']=4.74*ap.pml/ap.plx
ap['Vb']=4.74*ap.pmb/ap.plx
ap['U']=-ap.VHELIO_AVG*np.cos(ap.b)*np.cos(ap.l)+ap.Vl*np.sin(ap.l)+ap.Vb*np.cos(ap.l)*np.sin(ap.b)
ap['V']=-ap.VHELIO_AVG*np.cos(ap.b)*np.sin(ap.l)-ap.Vl*np.cos(ap.l)+ap.Vb*np.sin(ap.l)*np.sin(ap.b)
ap['W']=ap.VHELIO_AVG*np.sin(ap.b)+ap.Vb*np.cos(ap.b)
ap['R']=np.sqrt(ap.X*ap.X+ap.Y*ap.Y)


k=ap[(ap.plx>0) & (ap.plx_e/ap.plx<=0.4) & (np.sqrt(ap.X*ap.X+ap.Y*ap.Y)<20000) & (np.sqrt(ap.X*ap.X+ap.Y*ap.Y)>3000) & (np.abs(ap.Z)<3000) & (np.abs(ap.Z)>1000) & (np.abs(ap.FE_H)<5) & (np.abs(ap.MG_FE)<5) & (np.abs(ap.O_FE)<5) & (np.abs(ap.U)<400) & (np.abs(ap.V)<400) & (np.abs(ap.W)<400) & (ap.ALPHA_M>0.12) & (ap.FE_H>-2.5) & (ap.FE_H<-0.8) | (ap.plx>0) & (ap.plx_e/ap.plx<=0.4) & (np.sqrt(ap.X*ap.X+ap.Y*ap.Y)<20000) & (np.sqrt(ap.X*ap.X+ap.Y*ap.Y)>3000) & (np.abs(ap.Z)<3000) & (np.abs(ap.Z)>1000) & (np.abs(ap.FE_H)<5) & (np.abs(ap.MG_FE)<5) & (np.abs(ap.O_FE)<5) & (np.abs(ap.U)<400) & (np.abs(ap.V)<400) & (np.abs(ap.W)<400) & (ap.ALPHA_M-0.015>-0.0538*ap.M_H+0.0769) & (ap.M_H>-0.8) & (ap.M_H<0.5)]

k.to_csv('ThickDisk.csv')

###########################################################

plt.figure(1)
hb= plt.hexbin(k['X'], k['Y'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$X\,\,\,[pc]$')
plt.ylabel(r'$Y\,\,\,[pc]$')
plt.savefig('Thick_Disk_X_Y.png')

plt.figure(2)
hb= plt.hexbin(k['X'], k['Z'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$X\,\,\,[pc]$')
plt.ylabel(r'$Z\,\,\,[pc]$')
plt.savefig('Thick_Disk_X_Z.png')

plt.figure(3)
hb= plt.hexbin(k['Y'], k['Z'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$Y\,\,\,[pc]$')
plt.ylabel(r'$Z\,\,\,[pc]$')
plt.savefig('Thick_Disk_Y_Z.png')

plt.figure(4)
hb= plt.hexbin(k['U'], k['V'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$U\,\,\,[\frac{km}{s}]$')
plt.ylabel(r'$V\,\,\,[\frac{km}{s}]$')
plt.savefig('Thick_Disk_U_V.png')

plt.figure(5)
hb= plt.hexbin(k['U'], k['W'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$U\,\,\,[\frac{km}{s}]$')
plt.ylabel(r'$W\,\,\,[\frac{km}{s}]$')
plt.savefig('Thick_Disk_U_W.png')

plt.figure(6)
hb= plt.hexbin(k['V'], k['W'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$V\,\,\,[\frac{km}{s}]$')
plt.ylabel(r'$W\,\,\,[\frac{km}{s}]$')
plt.savefig('Thick_Disk_V_W.png')

plt.figure(7)
hb= plt.hexbin(k['M_H'], k['ALPHA_M'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$[M/H]$')
plt.ylabel(r'$[\alpha/H]$')
plt.savefig('Thick_Disk_MH_Alpha.png')

plt.figure(8)
hb= plt.hexbin(k['FE_H'], k['O_FE'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$[Fe/H]$')
plt.ylabel(r'$[O/Fe]$')
plt.savefig('Thick_Disk_Fe_O.png')

plt.figure(9)
hb= plt.hexbin(k['FE_H'], k['MG_FE'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$[Fe/H]$')
plt.ylabel(r'$[Mg/Fe]$')
plt.savefig('Thick_Disk_MG_FE.png')

plt.figure(10)
hb= plt.hexbin(k['R'], k['M_H'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$R\,\,[pc]$')
plt.ylabel(r'$[M/H]$')
plt.savefig('Thick_Disk_MH_R.png')

plt.figure(11)
hb= plt.hexbin(k['R'], k['ALPHA_M'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$R\,\,[pc]$')
plt.ylabel(r'$[\alpha/M]$')
plt.savefig('Thick_Disk_Alpha_R.png')

plt.figure(12)
hb= plt.hexbin(k['R'], k['O_FE'], gridsize=200, cmap='plasma')
cb = plt.colorbar(hb)
cb.set_label('Stars')
plt.xlabel(r'$R\,\,[pc]$')
plt.ylabel(r'$[O/Fe]$')
plt.savefig('Thick_Disk_O_R.png')

#plt.show()
