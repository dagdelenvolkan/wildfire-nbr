import rasterio
import numpy as np
from rasterio.enums import Resampling
import geopandas as gpd
import json
from rasterio.mask import mask
from shapely.geometry import box
from rasterio.plot import show
import matplotlib.pyplot as plt
from rasterio.plot import show_hist
import matplotlib
import seaborn as sns
import geopandas as gpd


def NBR_Calc(NIR, SWIR, output):
    #Calculating Normalized Burn Ratio Index
    NBR = (NIR.read().astype(float) - SWIR.read().astype(float)) / (NIR.read() + SWIR.read())
    meta = NIR.meta.copy()
    meta.update(driver='GTiff')
    meta.update(dtype=rasterio.float32)

    with rasterio.open(output, 'w', **meta) as dst:
        dst.write(NBR.astype(rasterio.float32))
        dst.close()