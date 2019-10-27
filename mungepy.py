import pandas as pd

def fillmedian(data):
    median = data.median()
    data.fillna(median, inplace = True)

def fillmode(data):
    mode = int(data.mode())
    data.fillna(mode, inplace = True)

def fillmean(data):
    mean = data.mean()
    data.fillna(mean, inplace = True)

