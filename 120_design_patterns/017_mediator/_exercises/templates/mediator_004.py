# """
# https://www.djangospin.com/design-patterns-python/mediator/
#
# Objects in a system communicate through a Mediator instead of directly with each other.
# This reduces the dependencies between communicating objects, thereby reducing coupling.
#
# *TL;DR
# Encapsulates how a set of objects interact.
# """
#
#
# c_ ChatRoom
#     """Mediator class"""
#
#     ___ display_message user message
#         print("[@ says]: @".f.. ?  ?
#
#
# c_ User
#     """A class whose instances want to interact with each other"""
#
#     ___ - name
#         ?  ?
#         chat_room = C..
#
#     ___ say message
#         c_r_.d_m.. ? ?
#
#     ___ -s
#         r_ n..
#
#
# ___ main
#     molly = U.. 'Molly'
#     mark = U.. 'Mark'
#     ethan = U.. 'Ethan'
#
#     mo__.s..("Hi Team! Meeting at 3 PM today.")
#     # [Molly says]: Hi Team! Meeting at 3 PM today.
#     ma__.s..("Roger that!")
#     # [Mark says]: Roger that!
#     et__.s..("Alright.")
#     # [Ethan says]: Alright.
#
#
#
# __ _______ __ ______
#     ?
