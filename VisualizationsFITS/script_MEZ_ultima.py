import numpy as np
from astropy.io import fits
import os
import matplotlib.pyplot as plt
import aplpy


__version__ = '1.0.6b'

"""
v1.0.6b: Added Recenter option to plot method.
"""


class FrameTools():
    def __init__(self, inFile):
        self.inFile = inFile
        
    def pixToVel(self, outName, linea, scale_=0.1755, vsys_=0.0):
        '''
        Este script es solo para transformar la longitud de onda en velocidad utiliaando
        los paramtros del Header de la imagen. Por tanto, el header debe contener lo 
        siguiente:
    
        --- VLSR
        --- EPOCH
        --- CCDUSM (o RBIN)
        --- VSYS (si se ha calculado, si no, sera 0)
        --- Y todos los campos de calibracion en lambda:
        ------------ CRVAL
        ------------ CDELT
        ------------ CRPIX
        ------------ CDX_X (x = 1,2)
        ------------ NAXIS
        ------------ DISPAXIS
    
        Inputs:
        -- inName = Nombre del archivo de entrada, con extensicion .fits
        -- outname = Nombre del archivo de salida, con o son .fits.
        -- scale_ = La escala de placa para BIN 1x1. Por ejemplo: MEZ, e2vm2, f/7
        -- linea = La linea de calibracion.
        -- vsys_ = Si no esta en el header, puedes darsela a mano, si no sera 0.0.
        resultaria en scale_ = 0.1755 arcsec/pix. Este ultimo es el valor por defecto.
    
        Output:
        -- Archivo con la dispersion en velocidad y la
    
        '''
        inFile = self.inFile
        # Intenta eliminar el archivo de salida, si es que existe, si no (OS Error)
        # no pasa nada.
    
        try:
            os.remove(outName)
        except OSError:
            pass
    
        # Abrimos el fits, en donde cada extension del fits es como un elemento de obejto
        # spec. Por eso, aunque solo tenga una extension, hay que llamarlo con [0], pues
        # python cuenta desde 0.
    
        spec = fits.open(inFile)
        head = spec[0].header
    
        # Obtenemos la escala que le hemos dado de comer a la definicion arriba.
        scale = scale_
    
        # La velocidad de la luz en km/s
        c = 299792.458
    
        disp = head["DISPAXIS"]
    
        # En algunos espectros (de muchoas anos atras, no existia el campo CCDSUM
        # por esta razon lo intento abrir, pero si no existe, entonces seguro son los
        # CBIN y RBIN los que te dicen el bin de los espectros.
    
        if "CCDSUM" in head:
            binning = head["CCDSUM"]
            bin1 = float(binning[0])
            bin2 = float(binning[2])
        elif "CBIN" in head or "RBIN" in head:
            bin1 = float(head["CBIN"])
            bin2 = float(head["RBIN"])
        else:
            raise ValueError("Binning keyword not found in header!.")
    
            # Checa cual es el eje de dispersion y con base en esto hace la
        # transformacion utilizando la scala que le has dado.
    
        try:
            vsys = float(head['VSYS'])
        except:
            vsys = vsys_
    
        # Lo que hace basicamente el siguiente script es convertir tanto wavelength en
        # velcoidad y pix a arcsec. Sin embargo, hay que tomar en cuenta que la imagen debe
        # esta recortada al gusto. Es decir, que NAXIS/2 realmente vaya a ser el cero
        # en arcsec. Si no es asi, no pasa nada, despues puedes sumarle a mano, con IRAF
        # al CRVAL de tal manera que el cero quede centrado en el centro geometrico de la
        # nebulosa. La velocidad depende unicamente de la lambda, por lo que si esta
        # recortada o no la imagen, no le importa, el calculo sera igualmente correcto.
        # Converting the plate scale.
        if disp == 2:
            head["CRVAL1"] = -(head["NAXIS1"] / 2.0) * scale * bin2
            head["CRPIX1"] = 0.0
            head["CD1_1"] = scale * bin2
            head["CDELT1"] = scale * bin2
            dv = (head["CDELT2"] / linea) * c
            head["CDELT2"] = dv
            head["CD2_2"] = dv
            # Corrected by VLSR and systemic
            v0 = (head["CRVAL2"] - linea) / linea * c + head["VLSR"] - vsys
            head["CRVAL2"] = v0
        else:
            head["CRVAL2"] = -(head["NAXIS2"] / 2.0) * scale * bin2
            head["CRPIX2"] = 0.0
            head["CD2_2"] = scale * bin2
            head["CDELT2"] = scale * bin2
            dv = (head["CDELT1"] / linea) * c
            head["CDELT1"] = dv
            head["CD1_1"] = dv
            # Corrected by VLSR and systemic
            v0 = (head["CRVAL1"] - linea) / linea * c + head["VLSR"] - vsys
            head["CRVAL1"] = v0
    
        spec.writeto(outName, overwrite=True)
    
    
    def plot_one_spec(self, spec_, dimensions_=[1, 0], vmin_=None, vmax_=None, show_=True,
                      save_=False, xlabel='Velocity (km/s)',
                      ylabel='Relative Postion (arcsec)', xspacing=None, yspacing=None,
		      recenter=None):
        '''
        spec = El espector ya calibrado
        dimensions = Orientacion de la imagen (v en x, o v en y). Valores
        [1,0], [0,1].
        vmin = Valor de grises minimo
        vmax = valor de grises maximo
        show = True para mostrar imagen
        sahve = True para guardar, aunque con el Show, puedes guardar desde el graficador.
        xlabel
        ylabel
    
        '''
    
        # Cargar el espectro creado, es decir el inName de la funcion anterior.
    
        fig = plt.figure(figsize=(6, 9))
        im = aplpy.FITSFigure(spec_, dimensions=dimensions_, figure=fig)
        im.show_grayscale(invert=True, vmin=vmin_, vmax=vmax_)
        im.set_theme('publication')
    
        im.axis_labels.set_xtext(xlabel)
        im.axis_labels.set_ytext(ylabel)
        im.tick_labels.set_font(size=11)
        # im.axis_labels.set_font(size="medium")
        im.ticks.set_xspacing(150)

        if xspacing:
            im.ticks.set_xspacing(xspacing)
        if yspacing:
            im.ticks.set_yspacing(yspacing)
        if recenter is not None:
            im.recenter(recenter[0], recenter[1])
        if recenter is not None:
            im.recenter(recenter[0], recenter[1], recenter[2], recenter[3])
        fig.savefig("kk.jpg", bbox_inches="tight", overwrite=True)
