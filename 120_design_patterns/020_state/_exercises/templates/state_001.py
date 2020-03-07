# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# Implementation of the state pattern
#
# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
#
# *TL;DR80
# Implements state as a derived class of the state pattern interface.
# Implements state transitions by invoking methods from the pattern's superclass.
# """
#
# ____ -f ______ p....
#
#
# c_ State o..
#
#     """Base state. This is to share functionality"""
#
#     ___ scan
#         """Scan the dial to the next station"""
#         pos +_ 1
#         __ ? __ le. s..
#             ? _ 0
#         print(u"Scanning... Station is @ @"
#               (s.. |? n..
#
#
# class AmState S...
#
#     ___ - radio
#         ?  ?
#         stations _ ["1250", "1380", "1510"]
#         pos _ 0
#         name _ "AM"
#
#     ___ toggle_amfm
#         print(u"Switching to FM")
#         r___.st.. _ r___.fm...
#
#
# c_ FmState S..
#
#     ___ - radio
#         ?  ?
#         stations _ ["81.3", "89.1", "103.9"]
#         pos _ 0
#         name _ "FM"
#
#     ___ toggle_amfm
#         print(u"Switching to AM")
#         r___.st.. _ r___.am..
#
#
# c_ Radio o..
#
#     """A radio.     It has a scan button, and an AM/FM toggle switch."""
#
#     ___ -
#         """We have an AM state and an FM state"""
#         amstate _ ? ?
#         fmstate _ ? ?
#         state _ a...
#
#     ___ toggle_amfm
#         s___.t_a..
#
#     ___ scan
#         s__.s..
#
#
# # Test our radio out
# __ ________ __ _______
#     radio _ ?
#     actions _ |?.s..| * 2 + |?.t_a.. + |?.s.. * 2
#     ? *_ 2
#
#     ___ action __ ?
#         ?
#
# ### OUTPUT ###
# # Scanning... Station is 1380 AM
# # Scanning... Station is 1510 AM
# # Switching to FM
# # Scanning... Station is 89.1 FM
# # Scanning... Station is 103.9 FM
# # Scanning... Station is 81.3 FM
# # Scanning... Station is 89.1 FM
# # Switching to AM
# # Scanning... Station is 1250 AM
# # Scanning... Station is 1380 AM
