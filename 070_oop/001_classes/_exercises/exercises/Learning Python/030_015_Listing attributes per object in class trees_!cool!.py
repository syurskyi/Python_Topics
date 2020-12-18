# ### File lister.py, continued
#
# c_ ListTree
#     """
#     Mix-in that returns an __str__ trace of the entire class
#     tree and all its objects attrs at and above self;
#     run by print(), str() returns constructed string;
#     uses __X attr names to avoid impacting clients;
#     uses generator expr to recurse to superclasses;
#     uses str.format() to make substitutions clearer
#     """
#     ___ -s ____
#         ____.__visited _       # dict
#         r_ '<Instance of @, address @ :\n @ @>'.f...(
#                            ____.-c.-n
#                            i. ____
#                            ____.__a.. ____ 0
#                            ____.__l.. ____.-c 4
#
#     ___ __listclass ____ aClass indent
#         dots = '.' * indent
#         __ aC.. __ ____.__v..
#             r_ '\n _ <Class _ :, address _ : (see above)>\n'.f...(
#                            d..
#                            a__. -n
#                            id a__
#         ____
#             ____.__v... aC.. _ T...
#             genabove _ ____.__l.. c, in..+4| ___ c __ aC__. -b|
#             r_ '\n @ <Class @ , address @ :\n @ @ @ >\n'.f...(
#                            d..
#                            a___. -n
#                            id aC__
#                            ____.__att.. a... in...
#                            ''.j... g..
#                            d...
#
#     ___ __attrnames ____ obj indent
#         spaces _ ' ' * (in.. + 4)
#         result _ ''
#         ___ attr __ so.. o. -d
#             __ a__.s_s_('__') an. a__.e.w. '__'
#                 r.. +_ s... + ' @ =<>\n'.f... a..
#             ____
#                 r___ + @ s___ + ' @ @ @# \n'.f... a... getattr o... a..
#         r_ r...
#
#
#
