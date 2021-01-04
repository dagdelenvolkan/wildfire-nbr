# This repository created for Spec. Top. in Rem. Sens. lecture and educational purposes.
</br>

# Goal
## This project aims to detect how to effect forest areas during the 2020 California Dolan Fire. To detect wildfire areas NBR (Normalized Burn Ratio) index has choosen and applied two time scale of ROI. 
</br>

# Dataset

### To apply NBR index pre and post data are required. In this case detection of start date of dolan wildfire is essential. Dolan fire started 18 August 2020.


## Choosen data
### Pre  --> 12 Augut 2020
### Post --> 11 October 2020
</br>

## Choosen dataset
### Sentinel-2A is choosen to implemented NBR index.
### All of these data are obtained from copernicus scihub to use educational purposes.
</br>


## NBR index
```
 NBR = (NIR - SWIR) / (NIR + SWIR)
```
</br>

## dnbr is used to detect changes.
```
dnbr = NBRpre - NBRpost
```
