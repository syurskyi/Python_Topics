from twisted.internet ______  reactor, protocol, endpoints
from twisted.internet.protocol ______  connectionDone


class ProcessClient(protocol.Protocol):

    def __init__(self, server):
        self.server _ server

    def connectionMade(self):
        print('Client connected...')
        self.server.concurrentClientCount +_ 1

    def connectionLost(self, reason_connectionDone):
        self.server.concurrentClientCount -_ 1

    def dataReceived(self, data: str):
        data _ data.strip()
        print('Data: ', data)
        self.transport.write(data)


class Server(protocol.Factory):
    commands _ ('init', 'send', 'get', 'close')

    def __init__(self):
        self.concurrentClientCount _ 0
        self.database _ {}

    def buildProtocol(self, addr):
        return ProcessClient(self)


server _ endpoints.serverFromString(reactor, 'tcp:8888')
server.l..(Server())
reactor.run()
