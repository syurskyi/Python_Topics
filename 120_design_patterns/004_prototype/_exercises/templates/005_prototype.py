# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# 
# """
# *TL;DR80
# Creates new object instances by cloning prototype.
# """
# 
# 
# c_ Prototype o..
# 
#     value _ 'default'
# 
#     ___ clone $$attrs
#         """Clone a prototype and update inner attributes dictionary"""
#         # Python in Practice, Mark Summerfield
#         obj _ ?. -c
#         ?. -d .up.. a..
#         r_ ?
# 
# 
# c_ PrototypeDispatcher o..
# 
#     ___ -
#         _o.. _     # dict
# 
#     ___ get_objects
#         """Get all objects"""
#         r_ _o..
# 
#     ___ register_object name obj
#         """Register an object"""
#         _o..|n.. _ ?
# 
#     ___ unregister_object name
#         """Unregister an object"""
#         de. _o..|n..
# 
# 
# ___ main
#     dispatcher _ PD..
#     prototype _ P..
# 
#     d _ p___.cl..
#     a _ p___.cl.. value_'a-value', category_'a')
#     b _ p___.cl.. value_'b-value', is_checked_True)
#     d___.r_o.. 'objecta', a
#     d___.r_o.. 'objectb', b
#     d___.r_o.. 'default', d
#     print n p.v... ___ ? ? __ d___.g_o___.i..
# 
# 
# __ ______ __ ______
#     ?
# 
# ### OUTPUT ###
# # [{'objectb': 'b-value'}, {'default': 'default'}, {'objecta': 'a-value'}]
