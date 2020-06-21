# """
# Flyweight Design Pattern
#    Desc: Sharing the shareable data between the common classes and thus
#    reducing the memory usage
#    Code: Believing that every person in a family will have same genetic
#          structure, we will create a code to learn about
#          genetics of each family. If a same member of a family is given, no new
#          object is created. (You can also create new
#          objects unlike here but keep a reference of the heavy weighted one in
#          the new |||r object).
# """
#
#
# c_ ComplexGenetics o..
#     """Returns a huge genetic pattern"""
#     ___ -
#         p..
#
#     ___ genes  gene_code
#         r_ "ComplexPatter[@]TooHugeinSize"  ?
#
#
# c_ Families o..
#     """To learn about Family Genetic Pattern."""
#     family     # dict
#
#     ___ -n ___ name family_id
#         """I have to capture the details before the class is created, __init__
#         is pseudo constructor."""
#         ___
#             id = ___.f..|f_i.
#         _____ K...
#             id = obj___. -n ___
#             ___.f...|f_i. _ ?
#         r_ ?
#
#     ___ set_genetic_info  genetic_info
#         cg _ C..
#         genetic_info _ ?.g.. ?
#
#     ___ get_genetic_info
#         r_ g_i.
#
#
# ___ test():
#     data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
#     family_objects _   # list
#     ___ i __ data
#         obj _ F.. ? 0 ? 1
#         ?.s_g_i.. ? |2
#         f_o_.ap.. ?
#
#     ___ i __ f_o..
#         print "id = " + st. i. ?
#         print ?.g_g_i..
#     print "similar id's says that they are same objects "
#
# __ _______ __ ______
#     test()
