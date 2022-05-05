# _______ p.... __ pd
# XYZ "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
# THRESHOLDS (5000, 0.05)
#
#
# ___ calculate_flux X.. s.. __ l..
#     """Read the data in from xyz.csv
#     add two new columns, one to calculate dollar flux,
#     and the other to calculate percentage flux
#     return as a list of tuples
#     """
#
#
#     data __.r.. X.. dtype_ '12/31/2020': i..,'12/31/2019': i..
#
#     ? 'dollar_flux'  = ? i.. |,1 .s.. ?i.. |,2
#     ? 'pct_flux'  = ?,i.. |,[-2,1]].p..(axis=1).dropna(axis=1)
#
#
#     r.. l.. ?.t.. index=F..
#
#
#
#
# ___ identify_flux xyz l.. __ l..
#     """Load the list of tuples, iterate through
#     each item and determine if it is above both
#     thresholds. if so, add to the list
#     """
#     flagged_lines    # list
#
#     ___ line __ ?
#         *orig,dollar_amount,pct_amount line
#         __ a.. d.. > T.. 0 a.. a.. p.. > T.. 1
#             f__.a.. ?
#
#     r.. ?
