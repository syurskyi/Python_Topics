# #!/usr/bin/python
# # Authoer: Spencer.Luo
# # Date: 11/26/2017
#
# # Version 1.0
# #=======================================================================================================================
# ____ a.. ______ A... a...
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Person m..
#     """people"""
#
#     ___ - name
#         _?  ?
#
#     ??
#     ___ wear
#         print("Dress code")
#
#
# c_ Engineer P..
#     """engineer"""
#
#     ___ - name skill
#         s___. - n..
#         __?  ?
#
#     ___ getSkill
#         r_ __s..
#
#     ___ wear
#         print("I'm " + ?g.. + "engineer " + _n.. en._"， ")
#         s__.w..
#
# c_ Teacher P..
#     "teacher"
#
#     ___  - name title
#         s___. - ?
#         __?  ?
#
#     ___ getTitle
#         r_ __t..
#
#     ___ wear
#         print("I'm " + _n.. + ?g.. en._"， ")
#         s__.w..
#
# c_ ClothingDecorator P..
#     """Base c_ for clothing decorators"""
#
#     ___ - person
#         _dec.. _ ?
#
#     ___ wear
#         _d___.w..
#         d..
#
#     ??
#     ___ decorate
#         p..
#
#
# c_ CasualPantDecorator(CD..
#     """Casual pants decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("One pair of khaki slacks")
#
#
# c_ BeltDecorator CD..
#     """Belt decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("Black belt with a silver pin buckle")
#
# c_ LeatherShoesDecorator CD..
#     """Leather shoe decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("A pair of dark casual leather shoes")
#
# c_ KnittedSweaterDecorator CD..
#     """Knitted sweater decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("A fuchsia knitted sweater")
#
#
# c_ WhiteShirtDecorator CD..
#     """White shirt decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("A white shirt")
#
#
# c_ GlassesDecorator CD...
#     """Glasses decorator"""
#
#     ___ - person
#         s__. - ?
#
#     ___ decorate
#         print("A pair of square black frame glasses")
#
#
#
#
# # Test
# #=======================================================================================================================
# ___ mainDecorator
#     tony = E..("Tony", "Client")
#     pant = CPD.. ?
#     belt = BD.. ?
#     shoes = LSD.. ?
#     shirt = WSD.. ?
#     sweater = KSD.. ?
#     glasses = GD.. ?
#     ?.w..
#
#     print()
#     decorateTeacher = GD.. WSD.. LSD.. T..."wells", "professor"
#     ?.w..
#
#
# ___ mainDecorator2
#     tony = E..("Tony", "Client")
#     sweater = KSD.. ?
#     shirt = WSD.. ?
#     glasses = GD.. ?
#     ?.w..
#
# mainDecorator()
# print()
# print('#' * 50)
# mainDecorator2()