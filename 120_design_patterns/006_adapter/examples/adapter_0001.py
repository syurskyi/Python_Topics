# Example #2: Square-pin to round-pin adapter
# Consider two incompatible interfaces: round-pin Socket & square-pin Electric Kettle.
# The Electric Kettle expects a square-pin connection for it to work.
# The Adapter takes square-pin of Electric Kettle, and connects to round-pin socket.

# Existing Class: a.k.a. Adaptee: Incompatible interface # 1
class Socket:
    _pinType = "Round"


# The Adapter: acts as an interface between two incompatible interfaces
class Adapter:
    _socket = None
    _pinType = "SquareToRound"

    def __init__(self, socket):
        self._socket = socket


# Client: Incompatible interface # 2
class ElectricKettle:
    _adapter = None
    _pinType = "Square"

    def __init__(self, adapter):
        self._adapter = adapter

    def makeTea(self):
        if self._adapter._pinType == (
                self._pinType + "To" + self._adapter._socket._pinType):  # "SquareToRound" == "Square" + "To" + "Round"
            print("Boiling water....")
            print("Adding ingredients...")
            print("Tea brewing...")
            print("Tea is ready!")
        else:
            print("No power. Can't function.")


# Create a socket
roundPinSocket = Socket()
# Connect adapter and socket
squareToRoundAdapter = Adapter(roundPinSocket)
# Connect Kettle and socket via adapter.
kettle = ElectricKettle(squareToRoundAdapter)

kettle.makeTea()

# OUTPUT:

# Boiling water....
# Adding ingredients...
# Tea brewing...
# Tea is ready!