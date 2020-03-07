# #=======================================================================================================================
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ ReceiveParcel m..
#     """Receive Parcel Abstract Class"""
#
#     ___ - name
#         __?  ?
#
#     ___  getName
#         r_ __name
#
#     ??
#     ___  receive parcelContent
#         p..
#
#
# # c_ TonyReception(ReceiveParcel):
# #     """Tony receives"""
# #
# #     def  - (self, name, phoneNum):
# #         super(). - (name)
# #         __phoneNum = phoneNum
# #
# #     def getPhoneNum(self):
# #         r_ __phoneNum
# #
# #     def receive(self, parcelContent):
# #         print("Cargo owner：@，phone number：@"  (getName(), getPhoneNum()) )
# #         print("Received a parcel，Package contents:@"  parcelContent)
# #
# #
# # c_ WendyReception(ReceiveParcel):
# #     """Wendy Collection"""
# #
# #     def  - (self, name, receiver):
# #         super(). - (name)
# #         __receiver = receiver
# #
# #     def receive(self, parcelContent
# #         print("I'm a friend of @, I'll help him collect the delivery!"  (__receiver.getName() + "") )
# #         __(__receiver is not None
# #             __receiver.receive(parcelContent)
# #         print("Income:@"  getName())
#
#
# # Version 2.0
# #=======================================================================================================================
# # Code framework
# #==============================
# ____ a.. ______ A.. a..
# # Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
#
# c_ Subject m..
#     """Theme class"""
#
#     ___ - name
#         __?  ?
#
#     ___  getName
#         r_ __?
#
#     ??
#     ___  request content _ ''
#         p..
#
#
# c_ RealSubject S..
#     """Real theme"""
#
#     ___  request content
#         print("RealSubject todo something...")
#
#
# c_ ProxySubject S..
#     """Agent theme class"""
#
#     ___ - name subject
#         s___. -  ?
#         _realSubject = ?
#
#     ___  request content _ ''
#         pR..
#         __ _r.. __ no. N..
#             _rS__.re.. ?
#         aR..
#
#     ___  preRequest
#         print("preRequest")
#
#     ___  afterRequest
#         print("afterRequest")
#
#
# # Framework-based implementation
# #==============================
#
# c_ TonyReception S..
#     """Tony receives"""
#
#     ___ - name phoneNum
#         s___. -  ?
#         __?  ?
#
#     ___  getPhoneNum
#         r_ __?
#
#     ___  request content
#         print("Cargo owner: @，phone number: @"  gN.. gP..
#         print("Received a package, package content: @"  st. ?
#
#
# c_ WendyReception P..
#     """Wendy Collection"""
#
#     ___ - name receiver
#         s___. - ?  ?
#
#     ___  preRequest
#         print("I'm a friend of @  I'll help him collect the delivery!"  (_rS__.gN.. + ""))
#
#     ___  afterRequest
#         print("Recipient: @"  gN..
#
#
# # Test
# #=======================================================================================================================
# ___  ReP..
#     tony = T..("Tony", "18512345678")
#     print("Tony receives:")
#     ?.r..("Snow boots")
#     print()
#
#     print("Wendy Collection:")
#     wendy = W..("Wendy", ?
#     ?.r..("Snow boots")
#
#
# ___  Proxy
#     realObj = R.. 'RealSubject'
#     proxyObj = P.. ('ProxySubject' ?
#     ?.r..
#
# ___  ReceiveParcel2
#     tony = T..("Tony", "18512345678")
#     print("Tony receives: ")
#     ?.r..("Snow boots")
#     print()
#
#     print("Wendy Collection:")
#     wendy = W.. "Wendy" ?
#     ?.r..("Snow Boots")
#
# # ReceiveParcel()
# # Proxy()
# RP..2
#
