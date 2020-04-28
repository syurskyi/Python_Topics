#
# """
# An example client. Run simpleserv.py first before running this.
# """
# ____ t__.i.. ______ rea.. pro..
# # a client protocol
#
# c_ EchoClient ?.P..
#     """Once connected, send a message, then print the result."""
#
#     ___ connectionMade
#         t__.w.. _"hello, world!"
#
#     ___ dataReceived data
#         "As soon as any data is received, write it back."
#         print ("Server said:" ?
#         t__.lC..
#
#     ___ connectionLost reason
#         print ("connection lost")
#
# c_ EchoFactory(?.CF..
#     protocol _ ?
#
#     ___ clientConnectionFailed connector reason
#         print ("Connection failed - goodbye!")
#         r__.s..
#
#     ___ clientConnectionLost connector reason
#         print ("Connection lost - goodbye!")
#         r__.s..
#
# # this connects the protocol to a server runing on port 8000
# ___ main
#     f _ EF..
#     ?.cT.. "localhost" 8000 ?
#     ?.r..
#
# # this only runs if the module was *not* imported
# __ _______ __ _______
#     ?