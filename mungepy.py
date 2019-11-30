import pandas as pd

# Filling NaN Values

def fillmedian(data):
    median = data.median()
    data.fillna(median, inplace = True)

def fillmode(data):
    mode = int(data.mode())
    data.fillna(mode, inplace = True)

def fillmean(data):
    mean = data.mean()
    data.fillna(mean, inplace = True)

def fillzero(data):
    data.fillna(0, inplace = True)

def fillone(data):
    data.fillna(1, inplace = True)


# Describing Data

def describemore(data):
    count = data.count()
    mean = data.mean()
    median = data.median()
    mode = data.mode()
    std = data.std()
    minimum = data.min()
    quarter = int(data.quantile([0.25]))
    half = int(data.quantile([0.50]))
    threequarters = int(data.quantile([0.75]))
    
    maximum = data.max()
    
    print('Count    ' + str(count))
    print('Mean     ' + str(mean))
    print('Median   ' + str(mean))
    print('Mode     ' + str(mean))
    print('Std      ' + str(std))
    print('Min      ' + str(minimum))
    print('25%      ' + str(quarter))
    print('50%      ' + str(half))
    print('75%      ' + str(threequarters))
    print('Max      ' + str(maximum))



