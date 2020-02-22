# #=======================================================================================================================
# ____ a.. ______ A.. a..m..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Coffee m...
#     """coffee"""
#
#     ___ -  name
#         .__?  ?
#
#     ___ getName
#         r_ __n..
#
#     ??
#     ___ getTaste
#         p..
#
#
# c_ LatteCaffe C..
#     """latte"""
#
#     ___ - name
#         s__ . - ?
#
#     ___ getTaste
#         r_ "Gentle and mellow"
#
# c_ MochaCoffee C..
#     """Mocha"""
#
#     ___ - name
#         s__ . - ?
#
#     ___ getTaste
#         r_ "Silky and mellow"
#
# c_ Coffeemaker
#     """Coffee machine"""
#
#     ??
#     ___ makeCoffee coffeeBean
#         "Define a static method with the staticmethod decorator"
#         __ ? __ "Latte coffee beans"
#             coffee _ L latte
#         ____ ? __ "Mocha coffee beans"
#             coffee _ M.. Mocha
#         ____
#             r_ V..("Unsupported parameters @"  ?
#         r_ c..
#
#
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ a.. ______ A.. a_m..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
# ____ e.. ______ E..
# # Python3.4 Enum syntax is supported afterwards
#
# c_ PenType E..
#     """Brush type"""
#     PenTypeLine = 1
#     PenTypeRect = 2
#     PenTypeEllipse = 3
#
#
# c_ Pen m..
#     """brush"""
#
#     ___ - name
#         __?  ?
#
#     ??
#     ___ getType
#         p..
#
#     ___ getName
#         r_ __n..
#
#
# c_ LinePen P..
#     """Straight brush"""
#
#     ___ - name
#         s__ . - ?
#
#     ___ getType
#         r_ PT_.PTL..
#
# c_ RectanglePen P..
#     """Rectangular brush"""
#
#     ___ - name
#         s__ . - ?
#
#     ___ getType
#         r_ PT__.PTR..
#
#
# c_ EllipsePen P..
#     """Oval brush"""
#
#     ___ -, name
#         s__. -?
#
#     ___ getType
#         r_ PT__.PTE..
#
#
# c_ PenFactory
#     """Brush factory c_"""
#
#     ___ -
#         "Define a dictionary (key: PenType, value: Pen) to store objects, and ensure that there will only be one object of each type"
#         ?__pens _    # dict
#
#     ___ getSingleObj penType name
#         """Get unique instance of object"""
#
#
#     ___ createPen penType
#         """Create brush"""
#         __ ?__p__.ge. ? __ N..
#             # If the object does not exist, an object is created and stored in the dictionary
#             __ ? __ PT__.pTL..
#                 pen _ L..("Straight brush")
#             ____ ? __ PT...PR..
#                 pen _ R.. ("Rectangular brush")
#             ____ ? __ PT...PTE..
#                 pen _ E.. ("Oval brush")
#             ____
#                 pen = P.. ""
#             __p__ pT.. _ pen
#         # Otherwise r_ the object in the dictionary directly
#         r_ .__p.. pT..
#
#
# # Framework-based implementation
# #==============================
#
#
# # Test
# #=======================================================================================================================
# ___ testCoffeeMaker
#     latte = C___.mC..("Latte coffee beans")
#     print("@ Ready for you, taste: @. Please enjoy slowly!"  ?.gN.. ?.gT..
#     mocha = C___.mC..("Mocha coffee beans")
#     print("@ is ready for you, taste: @. Please enjoy slowly!" ?.gN.. ?.gT..
#
#
# ___ testPenFactory
#     factory = P..
#     linePen = ?.cP.. PT...PTL..
#     print("created @，Object id: @， Types of:@" % (?.gN.. id ? ?.gT..
#     rectPen = ?.cP.. PT...PTR..
#     print("created @，Object id: @， Types of: @" % (?.gN.. id ? ?.gT..
#     rectPen2 = ?.cP.. PT...PTR..
#     print("created @，Object id: @， Types of:@" % (?.gN.. id ? ?.gT..
#     ellipsePen = ?.cP..( T...PTE..
#     print("created @，Object id: @， Types of: @" % (?.gN.. id ? eP__.gT..
#
#
# # testCoffeeMaker()
# testPenFactory()