#
# c_ E:
#     -s _ 'c', 'd'            # Superclass has slots
#
# c_ D E
#     -s _ 'a' '-d'     # So does its subclass
#
# X = D
# ?.a = 1; ?.b = 2; X.c = 3             # The instance is the union
# X.a, X.c
#
# E. -s                           # But slots are not concatenated
# D. -s
# X. -s                           # Instance inherits *lowest* __slots__
# X. -d                            # And has its own an attr dict
#
# ___ attr __ li.. g.. X '-d'|||| + g..  X ' -s' ||||
#     print a.. '=>', g.. X a..
#
# # b => 2                                    # Superclass slots missed!
# # a => 1
# # __dict__ => {'b': 2}
#
# dir(X)                                # dir() includes all slot names
