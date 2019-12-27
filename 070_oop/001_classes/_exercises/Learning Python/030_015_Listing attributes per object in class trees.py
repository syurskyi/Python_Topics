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
#         r_ '<Instance of _, address _ :\n _ _>'.f...(
#                            ____.-c.-n
#                            i. ____
#                            ____.__a.. ____ 0
#                            ____.__l.. ____.-c 4
#
#     ___ __listclass ____ aClass indent
#         dots = '.' * indent
#         i_ aClass i_ ____.__v..
#             r_ '\n _ <Class _ :, address _ : (see above)>\n'.f...(
#                            d..
#                            aC__. -n
#                            id aCl..
#         e___
#             ____.__v... aC.. _ T...
#             genabove _ ____.__l.. c, in..+4) ___ c i_ aC__. -b)
#             r_ '\n _ <Class _ , address _ :\n _ _ _ >\n'.f...(
#                            d..
#                            aC___. -n
#                            id aC..
#                            ____.__attrnames aC... in...
#                            ''.j... g..
#                            d...
#
#     ___ __attrnames ____ obj indent
#         spaces _ ' ' * (indent + 4)
#         result _ ''
#         ___ attr i_ so.. ?. -d
#             i_ a__.s_s_('__') an. a__.e.w. '__'
#                 result +_ s... + ' _ =<>\n'.f... a..
#             e___
#                 r___ +_ s___ + ' _ _ _ \n'.f... a... getattr o... a..
#         r_ r...
#
#
#
