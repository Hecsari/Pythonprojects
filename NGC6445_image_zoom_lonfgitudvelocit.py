import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from matplotlib.colors import LogNorm

hdulist = fits.open('N6445niilogespanav2.fits')
image_data = hdulist[0].data

# Get the dimensions of the image
xlength, ylength = image_data.shape

# Set the limits for the zoomed-in region in arcseconds
center_x, center_y = xlength / 2, ylength / 2
pixel_scale = 0.232  # arcseconds per pixel
x1, x2 = -160 * pixel_scale, 160 * pixel_scale
y1, y2 = -160 * pixel_scale, 160 * pixel_scale

# Set up the figure and plot the full image
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(image_data, cmap='gray_r', origin='lower', norm=LogNorm(vmin=0.5, vmax=4))
ax.set_xlabel('arcsec')
ax.set_ylabel('arcsec')

# Set the ticks and tick labels for the axes
xticks = np.arange(0, xlength, xlength / 10)
yticks = np.arange(0, ylength, ylength / 10)
xticklabels = np.round((xticks - center_x) * pixel_scale, 2)
yticklabels = np.round((yticks - center_y) * pixel_scale, 2)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_xticklabels(xticklabels)
ax.set_yticklabels(yticklabels)
ax.grid(color='black', linestyle='-', linewidth=0.5)

# Plot the zoomed-in region in a subplot
ax2 = fig.add_subplot(222)
ax2.imshow(image_data[int(center_y + y1 / pixel_scale):int(center_y + y2 / pixel_scale),
           int(center_x + x1 / pixel_scale):int(center_x + x2 / pixel_scale)],
           cmap='gray_r', origin='lower', extent=(x1, x2, y1, y2),
           norm=LogNorm(vmin=0.8, vmax=4))
ax2.set_xlabel('arcsec')
ax2.set_ylabel('arcsec')
ax2.grid(color='black', linestyle='-', linewidth=0.5)

fig.subplots_adjust(left=0.1, right=0.9, bottom=-1.0, top=-0.5, wspace=0.2, hspace=0.2)

plt.show()
fig.savefig('zoomedregion_NGC6445.eps')