from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os
%matplotlib inline
## make sure you set the DATA path to be to the folder where you downloaded the data at the beginning of class
DATA = "/Users/awong5/Desktop/landset/"

b4_raster = os.path.join(DATA, 'b4.tif')
b5_raster = os.path.join(DATA, 'b5.tif')

# Load in Red band
red_data = gdal.Open(b4_raster)
red_band = red_data.GetRasterBand(1)
red = red_band.ReadAsArray()

# Load in Near-infrasred band
nir_data = gdal.Open(b5_raster)
nir_band = nir_data.GetRasterBand(1)
nir = nir_band.ReadAsArray()

type(nir)

plt.imshow(nir)
plt.colorbar()

def ndvi_calc(red, nir):
    """ Calculate NDVI"""
    return (nir - red) / (nir + red)

plt.imshow(ndvi_calc(red, nir), cmap="YlGn")
plt.colorbar()

red.dtype
nir.dtype

red = red.astype(np.float32)
nir = nir.astype(np.float32)

plt.imshow(ndvi_calc(red, nir), cmap='YlGn')
plt.colorbar()

# Path of TIRS Band
b10_raster = os.path.join(DATA, 'b10.TIF')

# Load in TIRS Band
tirs_data = gdal.Open(b10_raster)
tirs_band = tirs_data.GetRasterBand(1)
tirs = tirs_band.ReadAsArray()
tirs = tirs.astype(np.float32)

# make this path the local path to your MTL.txt file that you downloaded at the start of the workshop
meta_file = '/Users/awong5/Desktop/landset/MTL.txt'

with open(meta_file) as f:
    meta = f.readlines()

# Define terms to match
matchers = ['RADIANCE_MULT_BAND_10', 'RADIANCE_ADD_BAND_10', 'K1_CONSTANT_BAND_10', 'K2_CONSTANT_BAND_10']

[s for s in meta if any(xs in s for xs in matchers)]

def process_string (st):
    return float(st.split(' = ')[1].strip('\n'))

matching = [process_string(s) for s in meta if any(xs in s for xs in matchers)]

rad_mult_b10, rad_add_b10, k1_b10, k2_b10 = matching

rad = rad_mult_b10 * tirs + rad_add_b10
plt.imshow(rad, cmap='RdYlGn')
plt.colorbar()

#Brightness temp
bt = k2_b10 / np.log((k1_b10/rad) + 1) - 273.15
plt.imshow(bt, cmap='RdYlGn')
plt.colorbar()
