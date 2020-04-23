# ch11/example3.py

______ a..

c_ EchoServerClientProtocol(?.Protocol):
    ___ connection_made(self, transport):
        peername _ transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport _ transport

    ___ data_received(self, data):
        message _ data.decode()
        print('Data received: {!r}'.format(message))

        self.transport.write(('Echoed back: {}'.format(message)).encode())

        print('Close the client socket')
        self.transport.close()

loop _ ?.g_e_l..
coro _ loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
server _ loop.r_u_c..(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
___
    loop.run_forever()
______ K..
    p..

# Close the server
server.close()
loop.r_u_c..(server.wait_closed())
loop.close()
