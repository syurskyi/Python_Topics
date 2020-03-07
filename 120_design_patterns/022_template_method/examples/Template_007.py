# # Version 1.0 Code framework
# #=======================================================================================================================
# ____ a.. _______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Template m..
#     """Template class (abstract class)"""
#
#     ?
#     ___ stepOne
#         p..
#
#     ?
#     ___ stepTwo
#         p..
#
#     ?
#     ___ stepThree
#         p..
#
#     ___ templateMethold
#         """Template method"""
#         ?
#         ?
#         ?
#
#
# c_ TemplateImplA T..
#     """Template implementation class A"""
#
#     ___ stepOne
#         print("step one")
#
#     ___ stepTwo
#         print("Step two")
#
#     ___ stepThree
#         print("Step three")
#
#
# c_ TemplateImplB T...
#     """Template implementation class B"""
#
#     ___ stepOne
#         print("Step one")
#
#     ___ stepTwo
#         print("Step two")
#
#     ___ stepThree
#         print("Step three")
#
#
# # Version 2.0 Reader view
# #=======================================================================================================================
# _____ a.. ________ A... a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ ReaderView m..
#     """Reader view"""
#
#     ___ -
#         __curPageNum _ 1
#
#     ___ getPage pageNum
#         __curPageNum _ ?
#         r_ "First" + st. ? + "Content"
#
#     ___ prePage
#         """Template method, page forward"""
#         content _ gP.. __c... - 1)
#         _dP.. ?
#
#     ___ nextPage
#         """Template method, page backward"""
#         content _ gP.. __c... + 1)
#         _dP.. ?
#
#     ?
#     ___ _displayPage content
#         """Page turning effect"""
#         p..
#
#
# c_ SmoothView R..
#     """Left and right smooth view"""
#
#     ___ _displayPage content
#         print("Smooth left and right:" + ?
#
#
# c_ SimulationView R..
#     """Flip page view"""
#
#     ___ _displayPage content
#         print("Page turning simulation:" + ?
#
#
# # Test
# #=======================================================================================================================
# ___ Reader
#     smoothView _ S..
#     ?.n..
#     ?.p..
#
#     simulationView _ S..
#     ?.n...
#     ?.p...
#
# ___ Template
#     templateA _ T..IA
#     ?.tM..
#     templateB _ T..IB
#     ?.tM..
#
#
# testReader()
# # testTemplate()