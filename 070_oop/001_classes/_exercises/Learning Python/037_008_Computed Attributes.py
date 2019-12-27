#
# C- DescSquare:
#     ___ - ____ start                  # Each desc has own state
#         ____.value _ start
#     ___ - ____ instance owner         # On attr fetch
#         r_ ____.va.. ** 2
#     ___ -s ____ instance, value         # On attr assign
#         ____.v.. _ v..                     # No delete or docs
#
# C- Client1
#     X = D___ 3         # Assign descriptor instance to class attr
#
# C- Client2
#     X = D___ 32         # Another instance in another client class
#                                # Could also code 2 instances in same class
# c1 = _1
# c2 = _2
#
# print(c1.X)                    # 3 ** 2
# c1.X = 4
# print(c1.X)                    # 4 ** 2
# print(c2.X)                    # 32 ** 2
#
