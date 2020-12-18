# ### file: setwrapper.py
#
# c_ Set
#    ___  -  value _    # Constructor  # List
#        ____.data _     # list                 # Manages a list
#        ____.concat v...
#
#    ___ intersect  other        # other is any sequence
#        res _    # list                      # self is the subject
#        ___ x __ ____.d..
#            __ x __ o..             # Pick common items
#                ?.ap.. x
#        r_ S.. ?                # Return a new Set
#
#    ___ union  other            # other is any sequence
#        res = ____.data               # Copy of my list
#        ___ x __ o...                # Add items in other
#            __ no. x __ ?
#                ?.ap... x
#        r_ S... ?
#
#    ___ concat  value          # value: list, Set...
#        ___ x __ ?                # Removes duplicates
#           __ no. x __ ____.d..
#                ____.d__.ap.. x
#
#    ___ -l
#        r_ le. ____.d..            # len(self)
#
#    ___ -g key
#        r_ ____.d.. k..            # self[i]
#
#    ___ -an  other
#        r_ ____.in... o..     # self & other
#
#    ___ -o other
#        r_ ____.un.. o..         # self | other
#
#    ___ -r
#        r_ 'Set:' + r.. ____.d..  # print()
#
#
# x = Set([1, 3, 5, 7])
# print(x.union(Set([1, 4, 7])))       # prints Set:[1, 3, 5, 7, 4]
# print(x | Set([1, 4, 6]))            # prints Set:[1, 3, 5, 7, 4, 6]
