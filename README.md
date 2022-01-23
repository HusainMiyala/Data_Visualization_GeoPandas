# Data_Visualization_GeoPandas
### Purpose

###### The purpose of this project is to visualize the generation of **Solar Power** in Canada between the time period of October 2021 - October 2021.

### Method

###### 1) Filter and retrieve Solar Power generation data in Canada using StatsCan repository and read file using Pandas.
###### 2) Download Canada .shape file from StatsCan repository and read file using GeoPandas library.
###### 3) Merge data frames on common column ID 'Province'.
###### 4) Plot .shape file and data using matplotlib library.

### Results

###### 1) Majority of Solar Power generated in Canada between October 2020 - October 2021 was in the province of Ontario.
###### 2) Solar Power generated is measured in Megawatt Hours (in one hundred thousands).

![](images/SolarPower_Canada.png)


### Setup

###### Required libraries include Pandas, Matplotlib, GeoPandas (Dependencies -> GDAL and Fiona)
###### Run on Python 3.8

### References

#### Canadian Solar Power Generation Data
###### Statistics Canada. Table 25-10-0015-01  Electric power generation, monthly generation by type of electricity

#### Canada .Shape files
###### Statistics Canada. https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2011-eng.cfm