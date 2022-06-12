# ____ c.. _______ n..
# ____ d__ _______ d__
#
# _______ p.... __ pd
#
# DATA_FILE "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
# STATION n..("Station", "ID Date Value")
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
#
#     """
#
#
#
#     stations __.r..("https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv",parse_dates= 'Date' )
#
#     stations 'Data_Value'  = ? 'Data_Value' .d.. 10
#     stations ? ~ ?.D__.d_.d.. __ 29 _ ?.D__.d_.m.. __ 2
#
#     s ? ?.D__.__.y.. !_ 2015
#
#     x ?.s.. Date
#
#
#     u s.g..  ID ?.D__.__.d.. .D__.a.. min max
#
#     s_2015 ? ?.D__.__.y.. __ 2015
#
#     records_2015 ?.g.. ID ?.D__.__.d.. .D__.a.. min max
#
#     ?.c.. =  2015_min 2015_max
#
#     l p_.c.. u ? a.._1
#
#     p l ? 2015_min  < ? min  | ? 2015_max  > ? max
#
#     ___ get_type_of_record_broken row
#
#         values    # list
#
#         __ ? 2015_min < ? min
#             ?.a.. ? 2015_min
#         __ ? 2015_max  > ? max
#             ?.a.. ? 2015_max
#         r.. ?
#
#     o p.a.. ? a.._1
#
#     n ?.e..
#
#     n ?.r..
#     ?.D.. pd.t.. ?.D.. f.._'%j'
#     ?.D.. ?.D__.a.. l.... x ?.r.. y.._2015
#
#
#     ? 0 ? 0 .a.. float
#
#
#     minimum ?.n.. 1 0 .T.s..
#     maximum ?.n.. 1 0 .T.s..
#
#     s1 S.. ?.I. ?.D.. ? 0
#     s2 S.. ?.I. ?.D.. ? 0
#
#     r.. ? ?
#
#
#
#
#
#
#
#
#
