# _______ __
# ____ p.. _______ P..
# ____ u__.r.. _______ u..
# ____ ___ _______ B..
# ____ c.. _______ d..
#
# # import the countries xml file
# tmp  P.. __.g.. "TMP", "/tmp"
# countries tmp / 'countries.xml'
#
# __ n.. ?.e..
#     u..
#         'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
#         ?
#
#
#
# ___ get_income_distribution ___=c..
#     """
#     - Read in the countries xml as stored in countries variable.
#     - Parse the XML
#     - Return a dict of:
#       - keys = incomes (wb:incomeLevel)
#       - values = list of country names (wb:name)
#     """
#     w__ o.. c.. _ __ f
#         contents ?.r..
#
#     soup B.. ? f.._'html.parser'
#     table ?.f.. 'wb:country'
#     d d.. l..
#
#     ___ tr __ t..
#         name ?.f.. 'wb:name' .t..
#         income ?.f.. 'wb:incomelevel' .t..
#         ? i__ .a.. ?
#
#     r.. d.. s.. d.i.. k.._l.... item ? 1