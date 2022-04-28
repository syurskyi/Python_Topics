# _______ p.... __ pd
#
# data "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
#
#
# ___ athletes_most_medals data s.. ? __ ?.S..
#
#     df __.r.. ?
#
#     # get medal counts for each athlete
#     g ?.g.. 'Athlete', 'Gender' .a.. 'Medal': 'count' .r..
#
#     # now group by gender and locate the max medal count by group, then
#     # drop Gender and squeeze into a series with index 'Athlete'
#     r.. ?.l.. g.g.. 'Gender') 'Medal'
#                  .i__ .d.. c.._'Gender' \
#             .s.. 'Athlete' .s.. a.._1
#
#
# __ _____ __ _____
#     print ?
