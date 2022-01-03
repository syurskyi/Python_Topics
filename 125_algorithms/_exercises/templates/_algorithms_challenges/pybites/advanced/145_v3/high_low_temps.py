____ collections _______ n..
____ d__ _______ date

_______ pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = n..("Station", "ID Date Value")

# df = pd.read_csv(DATA_FILE, parse_dates=['Date'])


___ remove_leap_days(df):
    '''removes leap days. This function assumes that the df is
    indexed by date.
    '''
    df.drop(df.index[(df.Date.dt.month __ 2) & (df.Date.dt.day __ 29)],
            inplace=T..)


___ prep_dfs(df):
    ''' This function prepares the df for use.
    It removes leap days and adds Month and Day columns.  It also separates out
    the 2015 data'''

    remove_leap_days(df)
    # Removing leap days doesn't change other day numbers--years will
    # still have days with number 366.  Add Month and Day columns to
    # the DF
    df['Month'] = df.Date.dt.month
    df['Day'] = df.Date.dt.day

    # separate data by date--2015 by itself
    df_ref = df[df.Date.dt.year != 2015]
    df_15 = df[df.Date.dt.year __ 2015]

    r.. df_ref, df_15


___ historical_records(df, element):
    '''Returns a DF of maximum (or min) temps for each day for each station
    element determines which to get. Possible values are 'TMIN' or 'TMAX'
    '''
    fun = 'min' __ element __ 'TMIN' ____ 'max'
    df = df[df.Element __ element]
    records = df.groupby(['Month', 'Day', 'ID']).agg({'Data_Value': fun})
    r.. records.reset_index()


___ merge_reduced(df1, df2):
    '''Merge df1 and df2 on Month, Day, ID with appropriate suffixes'''
    r.. pd.merge(df1, df2, on=['Month', 'Day', 'ID'],
                    suffixes=['_hist', '_15'])


___ series_to_station(ser):
    '''Creates a STATION tuple created from fields in pd.Series ser'''
    station = STATION(ser.ID,
                      date(ser.Date.year, ser.Date.month, ser.Date.day),
                      ser.Data_Value_15/10,
                      )
    r.. station



___ high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    """
    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])

    df_ref, df_15 = prep_dfs(df)

    # get the historical records (hi/low)
    lows = historical_records(df_ref, 'TMIN')
    highs = historical_records(df_ref, 'TMAX')

    # get the hi/low for 2015
    lows_15 = df_15[df_15.Element __ 'TMIN']
    highs_15 = df_15[df_15.Element __ 'TMAX']

    # merge reduced DFs based on month, day, ID for comparison
    lowmg = merge_reduced(lows, lows_15)
    highmg = merge_reduced(highs, highs_15)

    # Record breakers
    rb_low = lowmg[lowmg.Data_Value_15 < lowmg.Data_Value_hist]
    rb_high = highmg[highmg.Data_Value_15 > highmg.Data_Value_hist]

    # Get the min and max record breakers (these are series)
    rec_low = rb_low[rb_low.Data_Value_15 __ rb_low.Data_Value_15.m..()].iloc[0]
    rec_high = rb_high[rb_high.Data_Value_15 __ rb_high.Data_Value_15.max()].iloc[0]

    high = series_to_station(rec_high)
    low = series_to_station(rec_low)

    r.. high, low
