# This repository created for Spec. Top. in Rem. Sens. lecture and educational purposes.
</br>

![ITU](images/itu.jpg 'ITU')

# Goal
### This project aims to detect how to effect forest areas during the 2020 Austrilia Wildfire. To detect wildfire areas NBR (Normalized Burn Ratio) index has choosen and applied two time scale of ROI. 
</br>

# Dataset

### To apply NBR index pre and post data are required. In this case detection of start date of dolan wildfire is essential. Austrilia fire started January 2020.


## Choosen data
### Pre  -->  24 December 2019
### Post -->  12 April 2020
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
## NBR Images
![NBR](images/NBR.png 'NBR')


## Pre (24 December 2019) and Post (12 April 2020) NBR Histogram

![Histogram](images/hist.png 'Histogram')

## Severity Classes

| Severity Class | Range |
| :------------: | :---:|
|Unburned | < -0.1|
|Low Severity| < 0.27|
|Moderate-low Severity| < 0.44|
|Moderate-High Severity| < 0.66|
|High Severity| >= 0.66|

```
Severity Classes obtained from;
http://gsp.humboldt.edu/OLM/Courses/GSP_216_Online/lesson5-1/NBR.html
```
<br>

## Burn Severity
![Severity](images/burn_severity.png 'Severity')


## NBR Result with Legend
![Map](images/burn_result.png 'Result')

## Burn Serverity Ares with Hectares
<br>

| Severity Level | Area |
| :----: | :-:|
| High Severity | 3547.9 Hectares |
| Moderate-high Severity | 8583.7 Hectares |
| Moderate-low Severity | 12807.4 Hectares |
| Low Severity | 8464.63 Hectares |
| Unburned | 11596.4 Hectares |


