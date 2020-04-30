____ tw__.internet ______  reactor, protocol, endpoints
____ tw__.internet.protocol ______  connectionDone


c_ ProcessClient(protocol.Protocol):

    ___ - (self, server):
        self.server _ server

    ___ connectionMade
        print('Client connected...')
        self.server.concurrentClientCount +_ 1

    ___ connectionLost(self, reason_connectionDone):
        self.server.concurrentClientCount -_ 1

    ___ dataReceived(self, data: str):
        data _ data.strip()
        print('Data: ', data)
        self.transport.write(data)


c_ Server(protocol.Factory):
    commands _ ('init', 'send', 'get', 'close')

    ___ -
        self.concurrentClientCount _ 0
        self.database _ {}

    ___ buildProtocol(self, addr):
        r_ ProcessClient(self)


server _ endpoints.serverFromString(reactor, 'tcp:8888')
server.l..(Server())
reactor.run()
