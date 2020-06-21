# #!/usr/bin/env python
# # Written by: DGC
# 
# ______ a..
# 
# #==============================================================================
# c_ Singleton o..
#     """ A generic base class to derive any singleton class from. """
#     m..
#     __instance _ N..
# 
#     ___  -n new_singleton, $arguments $$keyword_arguments
#         """Override the __new__ method so that it is a singleton."""
#         __ n___.__? __ N..
#             n___.__? _ ob__. -n  n___
#             n___.__?.in.. $a.. $$k..
#         r_ n___.__?
# 
#     ??.?
#     ___ init  $arguments $$keyword_arguments
#         """ 
#         as __init__ will be called on every new instance of a base class of 
#         Singleton we need a function for initialisation. This will only be 
#         called once regardless of how many instances of Singleton are made.
#         """
#         r_
# 
# #==============================================================================
# c_ GlobalState S..
# 
#     ___ init
#         ?value = 0
#         print("init() called once")
#         print("")
# 
#     ___ -
#         print("__init__() always called")
#         print("")
# 
# c_ DerivedGlobalState G..
#     
#     ___ -
#         print("derived made")
#         s__D.. ____ . -
# 
#     ___ thing 
#         print .v..
# 
# #==============================================================================
# __ _____ __ _____
#     d = D..
#     print(t.. ?
#     ?.t..
#     ?.v.. = -20
#     e = D..
#     ?.t..
#     f = D..
#     ?.t...
#     
#     a = G..
#     # value is default, 0
#     print("Expecting 0, value = %i"  ?.v..
#     print("")
# 
#     # set the value to 5
#     ?.v.. = 5
# 
#     # make a new object, the value will still be 5
#     b = G..
#     print("Expecting 5, value = %i"  ?.v..
#     print("")
#     print("Is a == b? " + str(a == b))
