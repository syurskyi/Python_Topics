# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *What is this pattern about?
# The Decorator pattern is used to dynamically add a new feature to an
# object without changing its implementation. It differs from
# inheritance because the new feature is added only to that particular
# object, not to the entire subclass.
#
# *What does this example do?
# This example shows a way to add formatting options (boldface and
# italic) to a text by appending the corresponding tags (<b> and
# <i>). Also, we can see that decorators can be applied one after the other,
# since the original text is passed to the bold wrapper, which in turn
# is passed to the italic wrapper.
#
# *Where is the pattern used practically?
# The Grok framework uses decorators to add functionalities to methods,
# like permissions or subscription to an event:
# http://grok.zope.org/doc/current/reference/decorators.html
#
# *References:
# https://sourcemaking.com/design_patterns/decorator
#
# *TL;DR80
# Adds behaviour to object without affecting its class.
# """
#
# ____ -f ______ p..
#
# c_ TextTag o..
#     """Represents a base text tag"""
#     ___ - text
#         _?  ?
#
#     ___ render
#         r_ _t..
#
#
# c_ BoldWrapper T..
#     """Wraps a tag in <b>"""
#     ___ - wrapped
#         _?  ?
#
#     ___ render
#         r_ "<b>{}</b>".f.. _w___.r..
#
#
# c_ ItalicWrapper T..
#     """Wraps a tag in <i>"""
#     ___ - wrapped
#         _?  ?
#
#     ___ render
#         r_ "<i>{}</i>".f.. _w__.r..
#
# __ _______ __ ______
#     simple_hello = T..("hello, world!")
#     special_hello = I.. B.. ?
#     print("before:", si__.r..
#     print("after:", sp__.r..
#
# ### OUTPUT ###
# # before: hello, world!
# # after: <i><b>hello, world!</b></i>
