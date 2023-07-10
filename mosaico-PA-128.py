#!/usr/env python

import numpy
import aplpy
import pylab
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
import astropy.wcs
import astropy.io.fits

#Cargando imagenes
fig=plt.figure()
f1 = aplpy.FITSFigure("s1sp.fits", figure=fig,subplot=(1,2,1))
f1.show_grayscale( invert="True", vmin=1, vmax=10, stretch='log')
f2 = aplpy.FITSFigure("s1sp.fits", figure=fig,subplot=(1,2,2))
f2.show_grayscale( invert="True", vmin=10, vmax=10000, stretch='log')
#f3 = aplpy.FITSFigure("mes402234.fits", figure=fig,subplot=(1,3,3))
#f3.show_grayscale( invert="True", vmin=-5, vmax=80)

#cambiando parametros a imagenes
f1.set_theme("publication")
f2.set_theme("publication")
#f3.set_theme("publication")

#f1.recenter(0,0,width=280,height=174)

f1.ticks.set_xspacing(150)
f2.ticks.set_xspacing(150)
#f3.ticks.set_xspacing(140)
#f1.set_tick_labels_font(size=9)
#f1.set_axis_labels_font(size=11)
#f2.set_tick_labels_font(size=9)

#f2.set_axis_labels_font(size=11)

f1.axis_labels.hide_x()
f2.tick_labels.hide_y()
f2.axis_labels.hide()
#f3.tick_labels.hide_y()
#f3.axis_labels.hide()

#f1.axis_labels.set_xtext(r"Relative Velocity (km/s)")
f1.axis_labels.set_ytext(r"Relative Position (arcsec)")
fig.subplots_adjust(wspace=-0.2, hspace=0)
#f1.figtext(0.395,0.015,r'Radial Velocity (km/s)',rotation='horizontal', fontsize=10.4)

#Ponber labels

f1.add_label(120,73,'s13',size=14, weight="regular", family="sans-serif")
f1.show_arrows(-170, 68.5, 0, 10, color='black', width=2, head_width=20, length_includes_head=True)
f1.add_label(-130,73,'E',size=11, weight="regular")
f1.add_label(10,-70,'PA 90',size=11,)




#f3.add_label(120,73,'s13',size=14, fontweight="regular", fontfamily="sans-serif")
#f3.show_arrows(-175, 68.5, 0, 10, color='black', width=2, head_width=20, length_includes_head=True)
#f3.add_label(-125,73,'E',size=11, fontweight="regular")
#f3.add_label(10,-70,'PA 90',size=11)

plt.show()
