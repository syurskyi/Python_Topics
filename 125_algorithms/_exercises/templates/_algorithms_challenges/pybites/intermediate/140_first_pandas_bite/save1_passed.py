# _______ p.... __ pd
#
# data "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
#
#
# ___ athletes_most_medals data_?
#     df __.r.. ?
#
#     df_grouped ?.g.. 'Athlete', 'Gender' .c..
#     df_grouped ? 'Medal' .r..
#
#     mens ? ? 'Gender'  __ 'Men' .\
#         sort_values b._'Medal' a.._F.. .h.. 1
#     womens ? ? 'Gender'  __ 'Women' .\
#         s.. b._'Medal' a.._F.. .h.. 1
#
#     output __.m.. ? ? how='outer' 'Athlete', 'Medal' .\
#         s.. 'Athlete'
#     o.. ? 'Medal'
#     ?.i__.n.. N..
#
#     r.. ?.t..