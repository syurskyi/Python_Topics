# # Dependency Inversion Principle (DIP)
#
# # High-level objects should not depend on low-level implementation. Both should depend on abstractions.
# ____ a.. ______ a.. A..
# ____ ti.. ______ sl..
#
#
# c_ TurnableOnObject A..
#     ___ -
#         _on _ F..
#
#     ?p...
#     ___ on __ b..
#         r_ _o.
#
#     ?a..
#     ___ turn_on __ N..
#         p..
#
#
# c_ Lamp T..
#     ___ turn_on(
#         _on _ T..
#
#
# c_ TimedLamp L..
#     ___ turn_on
#         _o. _ T..
#         print("Waiting for 1 second before turning the lamp off.")
#         sl.. 1
#         _o. _ F..
#
#
# c_ OnButton
#     ___ - lamp L..
#         ??  ?
#
#     ___ press
#         __ no. ?l__.o.
#             ?l__.t...
#             print("The lamp has been turned on.")
#         ____
#             print("The lamp was already on.")
#
#
# __ _______ __ _____
#     lamp = L..
#     on_button = O.. ?
#     ?.p..
#     ?.p..
#     ?.p..
#
#     timed_lamp = T..
#     on_button_2 = O.. ?
#     # on_button_2.press()
#     # on_button_2.press()
