# ### file: setwrapper.py
#
# c_ Set:
#    ___  - ____ value_    # Constructor
#        ____.data _     # list                 # Manages a list
#        ____.concat v...
#
#    ___ intersect ____ other        # other is any sequence
#        res _    # list                      # self is the subject
#        ___ x i_ ____.data
#            i_ x i_ o..             # Pick common items
#                ?.ap.. x
#        r_ S.. ?                # Return a new Set
#
#    ___ union ____ other            # other is any sequence
#        res = ____.data               # Copy of my list
#        ___ x i_ o...                # Add items in other
#            i_ no. x i_ ?
#                ?.ap... x
#        r_ S... ?
#
#    ___ concat ____ value          # value: list, Set...
#        ___ x i_ v...                # Removes duplicates
#           i_ no. x i_ ____.data
#                ____.d__.ap.. x
#
#    ___ -l ____
#        r_ le. ____.d..            # len(self)
#
#    ___ -g ____ key
#        r_ ____.d.. k..            # self[i]
#
#    ___ -a ____ other
#        r_ ____.intersect o..     # self & other
#
#    ___ -o ____ other
#        r_ ____.union o..         # self | other
#
#    ___ -r ____
#        r_ 'Set:' + r.. ____.d..  # print()
#
#
# x = Set([1, 3, 5, 7])
# print(x.union(Set([1, 4, 7])))       # prints Set:[1, 3, 5, 7, 4]
# print(x | Set([1, 4, 6]))            # prints Set:[1, 3, 5, 7, 4, 6]
