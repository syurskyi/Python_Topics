
"""
An example client. Run simpleserv.py first before running this.
"""
____ twisted.internet ______ reactor, protocol
# a client protocol

c_ EchoClient(protocol.Protocol
    """Once connected, send a message, then print the result."""
    
    ___ connectionMade(self
        self.transport.w..(b"hello, world!")
    
    ___ dataReceived data
        "As soon as any data is received, write it back."
        print ("Server said:", data)
        self.transport.loseConnection
    
    ___ connectionLost re__on
        print ("connection lost")

c_ EchoFactory(protocol.ClientFactory
    protocol _ EchoClient

    ___ clientConnectionFailed connector, re__on
        print ("Connection failed - goodbye!")
        reactor.stop
    
    ___ clientConnectionLost connector, re__on
        print ("Connection lost - goodbye!")
        reactor.stop

# this connects the protocol to a server runing on port 8000
___ main
    f _ EchoFactory
    reactor.connectTCP("localhost", 8000, f)
    reactor.run

# this only runs if the module was *not* imported
__ _______ __ '__main__':
    main