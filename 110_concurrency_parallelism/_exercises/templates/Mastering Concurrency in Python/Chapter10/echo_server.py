______ a..

? ___ handle_echo(reader, writer):
    data _ await reader.read(100)
    message _ data.decode()
    addr _ writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Close the client socket")
    writer.close()

loop _ ?.get_event_loop()
coro _ ?.start_server(handle_echo, '127.0.0.1', 8888, loop_loop)
server _ loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
___
    loop.run_forever()
______ K..
    p..

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
