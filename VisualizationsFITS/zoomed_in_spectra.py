#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:31:39 2023

@author: hbello

"""
import aplpy
import matplotlib.pyplot as plt

# Load images
fig = plt.figure(figsize=(10, 24))
f1 = aplpy.FITSFigure("s6sp_newk2.fits", figure=fig, subplot=(1, 2, 1))
f2 = aplpy.FITSFigure("s6sp_newk2.fits", figure=fig, subplot=(1, 2, 2))

# Show grayscale image in f1 and overlay specific region on f2
f1.show_grayscale(invert=True, vmin=5, vmax=80, stretch='log')
f2.show_grayscale(invert=True, vmin=5, vmax=80, stretch='log')
f2.show_contour(f1._data, levels=[20, 50], colors='red', linewidths=1)
f2.recenter(0, -10, width=140, height=60)

# Set plot parameters
f1.set_theme("publication")
f2.set_theme("publication")
f1.ticks.set_xspacing(150)
f2.ticks.set_xspacing(150)
f1.axis_labels.set_xtext("km/s")
f1.axis_labels.set_ytext("arcsec")
f1.axis_labels.set_xposition('bottom')
f1.axis_labels.set_yposition('left')
f2.axis_labels.set_xtext("km/s")
f2.axis_labels.set_ytext("arcsec")
f2.axis_labels.set_xposition('bottom')
f2.axis_labels.set_yposition('left')

plt.show()
plt.savefig('zoomed_s6spnewk2_3.eps')
