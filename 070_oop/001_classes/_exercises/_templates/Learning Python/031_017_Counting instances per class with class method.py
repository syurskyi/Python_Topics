# c_ Spam
#     numInstances = 0
#     ___ count ___                    # Per-class instance counters
#         ___.n.. +_ 1          # cls is lowest class above instance
#     ___  - ____
#         ____.c...                   # Passes self.__class__ to count
#     count _ c... c..
#
# c_ Sub Sp..
#     numInstances = 0
#     ___  - ____                # Redefines __init__
#         Spam. - ____
#
# c_ Other Sp..                     # Inherits __init__
#     numInstances = 0
#
# x = ?
# y1, y2 = S.. S..
# z1, z2, z3 = O.. O... O..
# x.n..., y1.n..., z1.n...
#
# Spam.n..., Sub.n..., Other.n...
#
