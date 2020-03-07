
# """
# "Descriptors" section example of descriptor that will reveal its
#  access by printing information on stdout.
# 
# """
# 
# 
# c_ RevealAccess o..
#     """
#     A data descriptor that sets and returns values
#     normally and prints a message logging their access.
#     """
#     ___ - initval _ N.. name _ 'var'
#         val _ ?
#         ?  ?
# 
#     ___ -g obj objtype
#         print('Retrieving'  n..
#         r_ va.
# 
#     ___ -s obj val
#         print('Updating' n..
#         ?  ?
# 
# 
# c_ MyClass o..
#     x = R... (10, 'var "x"')
#     y = 5
# 
# 
# __ _______ __ _______
#     my_instance = M..
# 
#     # set x attribute (will issue print)
#     ?.x = 4
#     # access x attribute (will issue print)
#     ass.. ?.x __ 4
# 
#     # set y attribute (will pass silently)
#     ?.y = 2
#     # access x attribute (will pass silently)
#     ass.. ?.y __ 2
