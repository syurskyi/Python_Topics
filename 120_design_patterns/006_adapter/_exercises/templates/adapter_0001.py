# # Example #2: Square-pin to round-pin adapter
# # Consider two incompatible interfaces: round-pin Socket & square-pin Electric Kettle.
# # The Electric Kettle expects a square-pin connection for it to work.
# # The Adapter takes square-pin of Electric Kettle, and connects to round-pin socket.
#
# # Existing Class: a.k.a. Adaptee: Incompatible interface # 1
# c_ Socket
#     _pinType _ "Round"
#
#
# # The Adapter: acts as an interface between two incompatible interfaces
# c_ Adapter
#     _socket _ N..
#     _pinType _ "SquareToRound"
#
#     ___ - socket
#         _?  ?
#
#
# # Client: Incompatible interface # 2
# c_ ElectricKettle
#     _adapter _ N..
#     _pinType _ "Square"
#
#     ___ - adapter
#         _?  ?
#
#     ___ makeTea
#         __ _a___._p.. __ (
#                 _p... + "To" + _a____._s____._pT..):  # "SquareToRound" == "Square" + "To" + "Round"
#             print("Boiling water....")
#             print("Adding ingredients...")
#             print("Tea brewing...")
#             print("Tea is ready!")
#         else:
#             print("No power. Can't function.")
#
#
# # Create a socket
# roundPinSocket _ S..
# # Connect adapter and socket
# squareToRoundAdapter _ A... ?
# # Connect Kettle and socket via adapter.
# kettle _ E.. ?
#
# ?.mT..
#
# # OUTPUT:
#
# # Boiling water....
# # Adding ingredients...
# # Tea brewing...
# # Tea is ready!