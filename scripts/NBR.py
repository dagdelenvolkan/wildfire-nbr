import rasterio
import numpy as np



def NBR_Calc(NIR, SWIR, output):
    #Calculating Normalized Burn Ratio Index
    NBR = (NIR.read().astype(float) - SWIR.read().astype(float)) / (NIR.read() + SWIR.read())
    meta = NIR.meta.copy()
    meta.update(driver='GTiff')
    meta.update(dtype=rasterio.float32)

    with rasterio.open(output, 'w', **meta) as dst:
        dst.write(NBR.astype(rasterio.float32))
        dst.close()

def dnbr(preNBR, postNBR):
    dnbr = preNBR.read() - postNBR.read()
    meta = preNBR.meta.copy()
    meta.update(driver='GTiff')
    meta.update(dtype=rasterio.float32)

    with rasterio.open('dnbr.tif', 'w', **meta) as dst:
        dst.write(dnbr.astype(rasterio.float32))
        dst.close()

