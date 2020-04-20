from twisted.web.server ______ Site
from twisted.web.static ______ File
from twisted.internet ______ reactor, endpoints

resource = File('tmp')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
endpoint.listen(factory)
reactor.run()
