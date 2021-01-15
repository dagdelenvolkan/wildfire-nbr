# This repository created for Spec. Top. in Rem. Sens. lecture and educational purposes.
</br>

![ITU](images/itu.jpg 'ITU')

# Goal
### This project aims to detect how to effect forest areas during the 2020 Austrilia Wildfire. To detect wildfire areas NBR (Normalized Burn Ratio) index has choosen and applied two time scale of ROI. 
</br>

# Dataset

### To apply NBR index pre and post data are required. In this case detection of start date of dolan wildfire is essential. Austrilia fire started January 2020.

<br>

# Libraries

-rasterio
-matplotlib
-numpy
-seaborn

```
Libraries which are used in this project can be found in requirements.txt file with version numbers.
```

## Choosen data
### Pre  -->  24 December 2019
### Post -->  12 April 2020
</br>

## Chosen Area
### Austrilia's Buddong and Tumbarumba Area

<br>

## Choosen dataset
### Sentinel-2A is choosen to implemented NBR index.
### All of these data are obtained from copernicus scihub to use educational purposes.
</br>


## NBR index
```
 NBR = (NIR - SWIR) / (NIR + SWIR)
```

NBR index is usefull to detect Burning Ratio. NBR index is calculated to prefire and postfire images to decide change with dnbr.
</br>

## dnbr is used to detect changes.
```
dnbr = NBRpre - NBRpost
```
dnbr is used to understand how to change areas due to wildfire. Dnbr is a simply arithmetic subraction band operation to detect change.


<br>

## Work Flow
![WorkFlow](images/workflow.png 'WorkFlow')


## NBR Images
![NBR](images/NBR.png 'NBR')


## Pre (24 December 2019) and Post (12 April 2020) NBR Histogram

![Histogram](images/hist.png 'Histogram')

## Burn Severity Classes

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
Image below shows the burn severity areas as a white pixel to understand which areas are how effected.
![Severity](images/burn_severity.png 'Severity')


## NBR Result with Legend
![Map](images/burn_result.png 'Result')

## Burn Serverity Areas with Hectares
<br>

| Severity Level | Area |
| :----: | :-:|
| High Severity | 3547.9 Hectares |
| Moderate-high Severity | 8583.7 Hectares |
| Moderate-low Severity | 12807.4 Hectares |
| Low Severity | 8464.63 Hectares |
| Unburned | 11596.4 Hectares |

## Result

2020 was a bad year for Austrilia's people due to wildfire. In this project, burn severity detection is aimed with remote sensing methods and images. The result is shown above with images and tables to understand intuitively and logically. According to area of interest moderate-low level effect is more than others.
