# ____ p.. _______ P..
# ____ c.. _______ d..
# ____ u__.r.. _______ u..
# _______ ___.e__.E__ __ ET
#
# # import the countries xml file
# tmp  P..('/tmp')
# countries ? / 'countries.xml'
#
# __ n.. ?.e..
#     u..('https://bit.ly/2IzGKav' ?
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
#     tree __.p.. ___
#     root ?.g..
#     namespaces __: 'http://www.worldbank.org'
#
#     xpath f".//wb:country"
#     country_list d.. l..
#     ___ x __ r__.f.. x.. n..
#         ? ?.f.. 'wb:incomeLevel' n__ .t__ .a.. ?.f.. 'wb:name' n__.t..
#
#     r.. ?
