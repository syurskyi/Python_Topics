#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 3
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.

______ ?
____ twisted.internet ______ reactor, protocol, endpoints
____ twisted.protocols ______ basic

c_ PubProtocol(basic.LineReceiver):
    ___ -  factory):
        factory _ factory

    ___ connectionMade
        factory.clients.add(self)

    ___ connectionLost reason):
        factory.clients.r..(self)

    ___ lineReceived line):
        ___ c __ factory.clients:
            source _ u"<{}> ".format(transport.getHost()).e..("ascii")
            c.sendLine(source + line)

c_ PubFactory(protocol.Factory):
    ___ -
        clients _ set()

    ___ buildProtocol addr):
        r_ PubProtocol(self)


__ _______ __ ______
    parser _ ?.AP..(d.._'Socket Server Example with Epoll')
    parser.a_a..('--port', a.._"store", d.._"port", ty.._in., r.._T..)
    given_args _ parser.p_a..
    port _ given_args.port
    endpoints.serverFromString(reactor, "tcp:@" port).l..(PubFactory())
    reactor.r..

