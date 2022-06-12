# ____ c.. _______ n..
# ____ d__ _______ d__
#
# _______ p.... __ pd
#
# DATA_FILE "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
# STATION n..("Station", "ID Date Value")
#
# # df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
#
#
# ___ remove_leap_days df
#     '''removes leap days. This function assumes that the df is
#     indexed by date.
#     '''
#     ?.d.. ?.i.. ?.D__.dt.month __ 2) _ ?.D__.?.d.. __ 29
#             i.._T..
#
#
# ___ prep_dfs df
#     ''' This function prepares the df for use.
#     It removes leap days and adds Month and Day columns.  It also separates out
#     the 2015 data'''
#
#     ? ?
#     # Removing leap days doesn't change other day numbers--years will
#     # still have days with number 366.  Add Month and Day columns to
#     # the DF
#     ? Month  = ?.D__.__.m..
#     ? Day  = ?.D__.__.d..
#
#     # separate data by date--2015 by itself
#     df_ref ? ?.D__.__.y.. !_ 2015
#     df_15 ? ?.D__.__.y.. __ 2015
#
#     r.. ? ?
#
#
# ___ historical_records df element
#     '''Returns a DF of maximum (or min) temps for each day for each station
#     element determines which to get. Possible values are 'TMIN' or 'TMAX'
#     '''
#     fun 'min' __ ? __ TMIN ____ max
#     ? ? ?.E.. __ element
#     records ?.g.. Month Day ID .a.. Data_Value : fun
#     r.. ?.r..
#
#
# ___ merge_reduced df1 df2
#     '''Merge df1 and df2 on Month, Day, ID with appropriate suffixes'''
#     r.. __.m.. ? ? on= Month Day ID
#                     s.._ _hist _15
#
#
# ___ series_to_station ser
#     '''Creates a STATION tuple created from fields in pd.Series ser'''
#     station STATION ?.I_
#                       d.. ?.D__.y.. ?.D__.m.. ?.D__.d..
#                       ?.D../10
#
#     r.. ?
#
#
#
# ___ high_low_record_breakers_for_2015
#     """Extract the high and low record breaking temperatures for 2015
#
#     The expected value will be a tuple with the highest and lowest record
#     breaking temperatures for 2015 as compared to the temperature data
#     provided.
#
#     """
#     df __.r.. D..0 p.._ Date
#
#     d.. d.. p.. ?
#
#     # get the historical records (hi/low)
#     lows ? ? TMIN
#     highs ? ? 'MAX
#
#     # get the hi/low for 2015
#     lows_15 ? ?.E.. __ TMIN
#     highs_15 ? ?.E.. __ TMAX
#
#     # merge reduced DFs based on month, day, ID for comparison
#     lowmg ? l.. l..
#     highmg ? ? ?
#
#     # Record breakers
#     rb_low ? ?.D.. < ?.D..
#     rb_high ? ?.D.. > h__.D..
#
#     # Get the min and max record breakers (these are series)
#     rec_low ? ?.D.. __ ?.D__.m.. i.. 0
#     rec_high ? ?.D.. __ ?.D__.m.. i.. 0
#
#     high ? ?
#     low ? ?
#
#     r.. ? ?
