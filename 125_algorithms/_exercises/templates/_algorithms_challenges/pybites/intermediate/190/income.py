# _______ __
# _______ ___.e__.E__ __ ET
# ____ p.. _______ P..
# ____ u__.r.. _______ u..
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
#     country_incomes d.. l..
#     tree __.p.. ___
#     root ?.g..
#     ___ child __ ?
#         level ""
#         country ""
#         ___ ele __ c..
#             element ?.t.. ?.t__.r.. "}" +1| .l..
#
#             __ ? __ "incomelevel"
#                 level ?.t..
#             __ ? __ "name"
#                 country ?.t..
#
#         c.. l__ .a.. ?
#
#     r.. ?
#
# # if __name__ == "__main__":
# #     print(get_income_distribution())