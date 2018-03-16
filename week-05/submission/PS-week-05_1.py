from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np
import os
%matplotlib inline

DATA = "/Users/awong5/Desktop/landsat/"

def process_string (st):
    """
    Parses Landsat metadata
    """
    return float(st.split(' = ')[1].strip('\n'))

def ndvi_calc(red, nir):
    """
    Calculate NDVI
    """
    return (nir - red) / (nir + red)

def emissivity_calc (pv, ndvi):
    """
    Calculates an estimate of emissivity
    """
    ndvi_dest = ndvi.copy()
    ndvi_dest[np.where(ndvi < 0)] = 0.991
    ndvi_dest[np.where((0 <= ndvi) & (ndvi < 0.2)) ] = 0.966
    ndvi_dest[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ] = (0.973 * pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + (0.966 * (1 - pv[np.where((0.2 <= ndvi) & (ndvi < 0.5)) ]) + 0.005)
    ndvi_dest[np.where(ndvi >= 0.5)] = 0.973
    return ndvi_dest

def array2tif(raster_file, new_raster_file, array):
    """
    Writes 'array' to a new tif, 'new_raster_file',
    whose properties are given by a reference tif,
    here called 'raster_file.'
    """
    # Invoke the GDAL Geotiff driver
    raster = gdal.Open(raster_file)

    driver = gdal.GetDriverByName('GTiff')
    out_raster = driver.Create(new_raster_file,
                        raster.RasterXSize,
                        raster.RasterYSize,
                        1,
                        gdal.GDT_Float32)
    out_raster.SetProjection(raster.GetProjection())
    # Set transformation - same logic as above.
    out_raster.SetGeoTransform(raster.GetGeoTransform())
    # Set up a new band.
    out_band = out_raster.GetRasterBand(1)
    # Set NoData Value
    out_band.SetNoDataValue(-1)
    # Write our Numpy array to the new band!
    out_band.WriteArray(array)



location = "/Users/awong5/Desktop/landsat/"
def tif2array(location):
    # Load in band 1
    raster = os.path.join(location, 'LC08_L1TP_012030_20160830_20180130_01_T1_B10.tif')
    data = gdal.Open(raster)
    band = data.GetRasterBand(1)
    band_array = band.ReadAsArray()
    tirs = band_array.astype(np.float32)
    return tirs
    """
    Should:
    1. Use gdal.open to open a connection to a file.
    2. Get band 1 of the raster
    3. Read the band as a numpy array
    4. Convert the numpy array to type 'float32'
    5. Return the numpy array.
    """

#meta_text = '/Users/awong5/Desktop/landsat/LC08_L1TP_012030_20160830_20180130_01_T1_MTL.txt'
def retrieve_meta(meta_text):
    #meta_text = "/Users/awong5/Desktop/landsat/"
    txt = "LC08_L1TP_012030_20160830_20180130_01_T1_MTL.txt"
    file = meta_text + txt
    with open(file) as f:
        meta = f.readlines()
    matchers = ['RADIANCE_MULT_BAND_10', 'RADIANCE_ADD_BAND_10', 'K1_CONSTANT_BAND_10', 'K2_CONSTANT_BAND_10']
    var_list = [process_string(s) for s in meta if any(xs in s for xs in matchers)]
    return var_list
    """
    Retrieve variables from the Landsat metadata *_MTL.txt file
    Should return a list of length 4.
    'meta_text' should be the location of your metadata file
    Use the process_string function we created in the workshop.
    """

def rad_calc(tirs, var_list):
    rad = var_list[0] * tirs + var_list[1]
    return rad
    """
    Calculate Top of Atmosphere Spectral Radiance
    Note that you'll have to access the metadata variables by
    their index number in the list, instead of naming them like we did in class.
    """

def bt_calc(rad, var_list):
    bt = var_list[3] / np.log((var_list[3]/rad) + 1) - 273.15
    return bt
    """
    Calculate Brightness Temperature
    Again, you'll have to access appropriate metadata variables
    by their index number.
    """

def pv_calc(ndvi, ndvi_s, ndvi_v):
    pv = (ndvi - ndvi_s) / (ndvi_v - ndvi_s) ** 2
    """
    Calculate Proportional Vegetation
    """

def lst_calc(location):
    wave = 10.8E-06
    h = 6.626e-34
    c = 2.998e8
    s = 1.38e-23
    p = h * c / s
    tif2array(location)
    retrieve_meta(location)
    ndvi_calc(red, nir)

ndvi = ndvi_calc(red, nir)

    lst = bt / (1 + (wave * bt / p) * np.log(emissivity_calc(pv, ndvi)))
    """
    Calculate Estimate of Land Surface Temperature.
    Note that this should take as its input ONLY the location
    of a directory in your file system. That means it will have
    to call your other functions. It should:
    1. Define necessary constants
    2. Read in appropriate tifs (using tif2array)
    3. Retrieve needed variables from metadata (retrieve_meta)
    4. Calculate ndvi, rad, bt, pv, emis using appropriate functions
    5. Calculate land surface temperature and return it.
    Your LST function may return strips of low-values around the raster...
    This is a processing artifact that you're not expected to account for.
    Nothing to worry about!
    """
```
