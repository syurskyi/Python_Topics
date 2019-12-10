# c_ PropSquare
#     ___ - ____ start
#         ____.value = start
#     ___ getX ____                         # On attr fetch
#         r_ ____.v... ** 2
#     ___ setX ____ value                  # On attr assign
#         ____.v.. _ v..
#     X = pr... _X _X                # No delete or docs
#
# P = P... 3       # 2 instances of class with property
# Q = P... 32      # Each has different state information
#
# print(?.X)              # 3 ** 2
# P.X = 4
# print(?.X)              # 4 ** 2
# print(Q.X)              # 32 ** 2
#
