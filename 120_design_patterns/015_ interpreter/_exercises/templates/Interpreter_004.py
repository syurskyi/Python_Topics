# #!/usr/bin/env python
# # Written by: DGC
#
# import re
#
# #==============================================================================
# c_ CamelCase o..
#
#     ___ -
#         SomeProperty _ "A property"
#
#     ___ SomeMethod argument
#         print ?
#
# #==============================================================================
# c_ CamelCaseInterpreter o..
#
#     ___ - old_class
#         s___ C.., ? . -s ("__old_class" ?
#
#     ___ __getattribute__ name
#         old_class _ s___ C.. ? . -g ("__old_class")
#         converter _ s___ C.. ? . -g ("name_converter")
#         r_ o_c__. -g  con.. n..
#
#     ___ -s name value
#         old_class _ s___ C.. ? . -g ("__old_class")
#         converter _ s___ C.. ? . -g ("name_converter")
#         ?. -s  c.. n.. v..
#
#     ___ name_converter name
#         """
#         Converts function/property names which are lowercase with underscores
#         to CamelCase. i.e some_property becomes SomeProperty.
#         """
#         new_name _ n.. 0 .up..
#         previous_underscore _ ? __ "_"
#         ___ char __ n..|1;
#             __ ? __ "_"
#                 p_u.. _ T..
#             ____
#                 __ p_u..
#                     n_n.. +_ ?.up..
#                 ____
#                     n_n.. +_ ?
#                 p_u.. _ F..
#         r_ n_n..
#
# #==============================================================================
# __ _______ __ ______
#     old_class _ C..
#
#     interpreted_class _ C.. ?
#     print i_c_.s_p..
#
#     i_c__.s_p.. _ "Newly set property"
#     print(i_c__.s_p..
#
#     i_c__.s_m..("Argument to some_method")
#
