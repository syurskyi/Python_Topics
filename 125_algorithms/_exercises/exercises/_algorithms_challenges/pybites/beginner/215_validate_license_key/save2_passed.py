# _______ __
#
#
# ___ validate_license key s..  __ b..
#     """Write a regex that matches a PyBites license key
#        (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
#     """
#     start  b.. __.m.. _'^PB' ?
#     split_count  a.. b.. x
#                       ___ ? __ l.. entry  __ 8
#                                 ___ ? __ ?.s.. '-' 1|
#     character_check  b..(
#         __.m.. '^[a-zA-Z0-9]+$' ''.j.. ?.s.. '-' 1|
#     r.. s.. s.. c