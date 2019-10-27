# MungePy

MungePy is a set of tools used for wrangling and cleaning messy data. I have created these functions in order to cut down on time spent replacing values, cleaning data, and other common tasks used when preparing data. 

## Getting Started

No need to install this library, just download the files into your working directory. You will however need to make sure that you have **pandas** installed.

## Requirements
- Python 3.X  https://www.python.org/downloads/
- Pandas https://pandas.pydata.org/pandas-docs/stable/install.html

## User Guide

### Replacing NaN Values

We use the **fillna()** function from pandas here, but we have made it easier and less time consuming to fill in NaN values using meadian, mean, mode. The values as set *inplace = True*.

**fillmedian()**

We use the fillmedian() function fills in NaN values with the median for a given column.

```
df = dataframe
fillmedian(df['column_name']) 
```
**fillmean()**

We use the fillmean() function fills in NaN values with the mean for a given column.

```
df = dataframe
fillmean(df['column_name']) 
```

**fillmode()**

We use the fillmode() function fills in NaN values with the mode for a given column.

```
df = dataframe
fillmode(df['column_name']) 
```
### Describing Data

**describemore()**

The describemore() feature is very similar to the describe() function in pandas but it give more information, including median and mode.

```
df = dataframe
descrbemore(df['column_name'])
```

```
Count    9
Mean     3.0
Median   3.0
Mode     3.0
Std      1.9364916731037085
Min      1.0
25%      1
50%      3
75%      5
Max      6.0
```




