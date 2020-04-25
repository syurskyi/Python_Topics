____ twisted.internet ______ reactor, protocol

c_ Echo(protocol.Protocol
    """This is just about the simplest possible protocol"""
    
    ___ dataReceived(self, data
        "As soon as any data is received, write it back."
        self.transport.w..(data)
        print(data)

___ main
    """This runs the protocol on port 8000"""
    factory _ protocol.ServerFactory
    factory.protocol _ Echo
    reactor.l..TCP(8000,factory)
    reactor.run

# this only runs if the module was *not* imported
__ _______ __ '__main__':
    main