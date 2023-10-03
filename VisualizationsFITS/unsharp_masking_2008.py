import numpy as np
from astropy.io import fits
from astropy.convolution import convolve, Gaussian2DKernel, convolve_fft
from scipy.signal import convolve as scipy_convolve                                                         
import matplotlib.pyplot as plt                                        
import aplpy                                                           

img, header = fits.getdata("s2_new.fits", header=True)
dimensions_= [0,1]

std_x = 3*(3.125/np.sqrt(8*np.log(2)))
std_y  = 3*(4.24/np.sqrt(8*np.log(2)))
kernel = Gaussian2DKernel(x_stddev=std_x, y_stddev=std_y, mode="linear_interp")

img[img > 62000] = 0.0
img[img == 0.0] = np.nan
conv = convolve(img, kernel)
# imgz = img.copy()
# imgz[np.isnan(imgz)] = 0.0
# print("Before convolution.")
# conv = scipy_convolve(imgz, kernel, mode="same", method="direct")
# print("After convolution.")
new = img - conv

hdu = fits.PrimaryHDU(new, header)
hdul = fits.HDUList([hdu])
hdul.writeto("s2sp_newk2.fits", overwrite=True)                                    
                             
