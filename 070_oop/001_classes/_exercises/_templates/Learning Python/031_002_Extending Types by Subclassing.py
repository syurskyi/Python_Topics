# ### file: typesubclass.py
#
# # Subclass built-in list type/class
# # Map 1..N to 0..N-1; call back to built-in version.
#
# c_ MyList li..
#     ___ -g  offset
#         print('(indexing @ at @)' @  ____ ?
#         r_ li__. -g ____ ? - 1)
#
# __ _____ __ _____
#     print(li.. ('abc'))
#     x = ? abc              # __init__ inherited from list
#     print(x)                        # __repr__ inherited from list
#
#     print(x[1])                     # MyList.__getitem__
#     print(x[3])                     # Customizes list superclass method
#
#     x.ap.. spam; print(x)      # Attributes from list superclass
#     x.re.. ;print(x)
#
#
# ### file: setsubclass.py
#
# c_ Set li..
#     ___  -  value _     # list      # Constructor
#         li__. - |                # Customizes list
#         ____.co.. v..               # Copies mutable defaults
#
#     ___ intersect ____ other          # other is any sequence
#         res _    # list                         # ____ is the subject
#         ___ x __ ____
#             __ x __ o...               # Pick common items
#                 ?.ap.. x
#         r_ S.. ?                  # Return a new Set
#
#     ___ union ____ other              # other is any sequence
#         res _ S.. ____                  # Copy me and my list
#         ?.co.. o.
#         r_ ?
#
#     ___ concat ____ value             # value: list, Set . . .
#         ___ x __ ?                  # Removes duplicates
#             __ no. x __ ____
#                 ____.ap.. x
#
#     ___ -a  ____ other r_ ____.in... o..
#     ___ -o ____ other  r_ ____.un.. o..
#     ___ -r ____       r_ 'Set:' + li__. -r ____
#
# __ _______ __ _______
#     x = Set([1,3,5,7])
#     y = Set([2,1,4,5,6])
#     print(x, y, len(x))
#     print(x.intersect(y), y.union(x))
#     print(x & y, x | y)
#     x.reverse(); print(x)