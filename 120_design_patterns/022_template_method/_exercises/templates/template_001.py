# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
#
# An example of the Template pattern in Python
#
# *TL;DR80
# Defines the skeleton of an algorithm, deferring steps to subclasses.
# """
#
# ingredients _ "spam eggs apple"
# line _ '-' * 10
#
#
# # Skeletons
# ___ iter_elements getter action
#     """Template skeleton that iterates items"""
#     ___ element __ ?
#         a.. ?
#         print l..
#
#
# ___ rev_elements getter action
#     """Template skeleton that iterates items in reverse order"""
#     ___ element __ ? ;;-1
#         a.. ?
#         print l..
#
#
# # Getters
# ___ get_list
#     r_ i___.sp..
#
#
# ___ get_lists
#     r_ li.. x ___ x __ i___.sp..
#
#
# # Actions
# ___ print_item item
#     print ?
#
#
# ___ reverse_item item
#     print ? ;;-1
#
#
# # Makes templates
# ___ make_template skeleton getter action
#     """Instantiate a template method with getter and action"""
#     ___ template
#         s.. ?  ?
#     r_ ?
#
# # Create our template functions
# templates _ |? s, g, a)
#              ___ g __ g.. g...
#              ___ a __ p.. r..
#              ___ s __ i.. r..
#
# # Execute them
# ___ template __ ?
#     ?
#
# ### OUTPUT ###
# # spam
# # ----------
# # eggs
# # ----------
# # apple
# # ----------
# # apple
# # ----------
# # eggs
# # ----------
# # spam
# # ----------
# # maps
# # ----------
# # sgge
# # ----------
# # elppa
# # ----------
# # elppa
# # ----------
# # sgge
# # ----------
# # maps
# # ----------
# # ['s', 'p', 'a', 'm']
# # ----------
# # ['e', 'g', 'g', 's']
# # ----------
# # ['a', 'p', 'p', 'l', 'e']
# # ----------
# # ['a', 'p', 'p', 'l', 'e']
# # ----------
# # ['e', 'g', 'g', 's']
# # ----------
# # ['s', 'p', 'a', 'm']
# # ----------
# # ['m', 'a', 'p', 's']
# # ----------
# # ['s', 'g', 'g', 'e']
# # ----------
# # ['e', 'l', 'p', 'p', 'a']
# # ----------
# # ['e', 'l', 'p', 'p', 'a']
# # ----------
# # ['s', 'g', 'g', 'e']
# # ----------
# # ['m', 'a', 'p', 's']
# # ----------
