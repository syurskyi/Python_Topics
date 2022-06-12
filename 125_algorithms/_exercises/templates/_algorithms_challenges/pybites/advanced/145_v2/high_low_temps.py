# _______ c__
# _______ __
# _______ __
# _______ u__.r..
# ____ c.. _______ n..
# ____ d__ _______ d__
#
# _______ p.... __ pd
#
# DATA_FILE "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
# STATION n..("Station", "ID Date Value")
#
# TMP '/tmp'
# LOCAL_FILE __.p...j..('/tmp', 'weather-ann-arbor.csv')
# __ n.. __.p...i.. ?
#     u__.r...u.. D.. L..
#
#
# ___ high_low_record_breakers_for_2015
#     """Extract the high and low record breaking temperatures for 2015
#
#     The expected value will be a tuple with the highest and lowest record
#     breaking temperatures for 2015 as compared to the temperature data
#     provided.
#
#     NOTE:
#     The date values should not have any timestamps, should be a
#     datetime.date() object. The temperatures in the dataset are in tenths
#     of degrees Celsius, so you must divide them by 10
#
#     Possible way to tackle this challenge:
#
#     1. Create a DataFrame from the DATA_FILE dataset.
#
#     2. Manipulate the data to extract the following:
#        * Extract highest temperatures for each day / station pair between 2005-2015
#        * Extract lowest temperatures for each  day / station  between 2005-2015
#        * Remove February 29th from the dataset to work with only 365 days
#
#     3. Separate data into two separate DataFrames:
#        * high/low temperatures between 2005-2014
#        * high/low temperatures for 2015
#
#     4. Iterate over the 2005-2014 data and compare to the 2015 data:
#        * For any temperature that is higher/lower in 2015 extract ID,
#          Date, Value
#
#     5. From the record breakers in 2015, extract the high/low of all the
#        temperatures
#        * Return those as STATION namedtuples, (high_2015, low_2015)
#     """
#     w__ o.. L.. __ f
#         the_data s..
#              id : x ?
#             date : d__.s.. ? Date  _Y-_m-_d .d..
#             element : ? Element
#             value : i.. ? Data_Value
#          ___ ? __ c__.D.. ? __ n.. __.m.. _ \d{4}-02-29 ? Date
#             k.._l.... x| ? id  + ? date .s.. _m_d_Y
#     dataset id : ? id
#                 monthday : ? date .s.. _m_d
#                 year : ? date .y..
#                 element : ? element
#                 value : ? value
#                  ___ ? __ ?
#
#     data_before_2015_left __.D.. x ___ ? __ ? __ ? year  < 2015 a.. ? element  __ TMIN .d..
#          element year axis_1 .s.. id monthday .g..
#          id monthday .m.. l.._ monthday .r.. c.._ value : mina
#
#     data_before_2015_right __.D.. x ___ ? __ ? __ x year  < 2015 a.. ? element  __ TMAX .d..
#          element year a.._1 .s.. id monthday .g..
#          id monthday .m.. l.._ monthday.r.. c.._ value : maxa
#
#     early_dataset ?.j.. ? lsuffix_'_l' rsuffix='_r'
#
#     data_for_2015_left __.D.. x ___ ? __ ? __ ? year  __ 2015 a.. ? element  __ TMIN .d..
#          element year  a.._1 .s.. id monthday .g..
#          id monthday .m.. l.._ m__.r.. columns_ value : minb
#
#     data_for_2015_right __.D.. x ___ ? __ ? __ ? year  __ 2015 a.. ? element  __ TMAX .d..
#          element year  a.._1 .s..  id monthday .g..
#          id monthday .m.. l.._ m__.r.. columns_ value : maxb
#
#     late_dataset ?.j.. ?
#
#     compare_set e__.j.. ?
#
#     result min :    # list, 'max': []}
#     ___ row __ ?.i..
#         __ ?.m.. > ?.m..
#             ? m.. .a..
#                 S.. ?.? 0 d__.s.. _*2015 ?.? 1  _Y_m_d .d.. ?.m.. / 10.0
#         __ ?.m.. < ?.m..
#             r.. m.. .a..
#                 S.. ?.? 0 d__.s.. _*2015 ?.? 1 _Y_m_d .d.. ?m.. / 10.0
#
#     r.. m.. ? max k.._l.... ?| ?.V.. m.. r.. min k.._l.... x| ?.V..
