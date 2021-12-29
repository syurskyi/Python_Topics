from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


___ high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10


    """



    stations = pd.read_csv("https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv",parse_dates=['Date'])
    
    stations['Data_Value'] = stations['Data_Value'].div(10)
    stations = stations[~((stations.Date.dt.day == 29) & (stations.Date.dt.month == 2))]

    s = stations[stations.Date.dt.year != 2015]

    x = stations.set_index('Date')


    u = s.groupby(['ID',s.Date.dt.dayofyear]).Data_Value.agg(['min','max'])

    s_2015 = stations[stations.Date.dt.year == 2015]

    records_2015 = s_2015.groupby(['ID',s_2015.Date.dt.dayofyear]).Data_Value.agg(['min','max'])

    records_2015.columns = ['2015_min','2015_max']

    l = pd.concat([u,records_2015],axis=1)

    p = l[(l['2015_min'] < l['min']) | (l['2015_max'] >l['max'])]

    ___ get_type_of_record_broken(row):
        
        values = []
        
        __ row['2015_min'] < row['min']:
            values.append(row['2015_min'])
        __ row['2015_max'] > row['max']:
            values.append(row['2015_max'])
        return values

    o = p.apply(get_type_of_record_broken,axis=1)

    n = o.explode()

    n = n.reset_index()
    n.Date = pd.to_datetime(n.Date,format='%j')
    n.Date = n.Date.apply(lambda x: x.replace(year=2015))


    n[0] = n[0].astype('float')


    minimum = n.nsmallest(1,0).T.squeeze()
    maximum = n.nlargest(1,0).T.squeeze()
    
    s1 = STATION(minimum.ID,minimum.Date,minimum[0])
    s2 = STATION(maximum.ID,maximum.Date,maximum[0])

    return s2,s1









