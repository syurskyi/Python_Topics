#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 7
# This program is optimized for Python 2.7.12.
# Supervisor requires Python 2.x, and does not run on Python 3.x.


______ supervisor.xmlrpc
______ xmlrpclib

___ query_supervisr(sock):
    transport _ supervisor.xmlrpc.SupervisorTransport(N.., N..,
                'unix://@' sock)
    proxy _ xmlrpclib.ServerProxy('http://127.0.0.1',
            transport_transport)
    print ("Getting info about all running processes via Supervisord...")
    print (proxy.supervisor.getAllProcessInfo())

__ _______ __ ______
    query_supervisr(sock_'/tmp/supervisor.sock')
    

