# ch18/example6.py

______ socket, select, types
____ collections ______ namedtuple
____ operator ______ mul
____ functools ______ reduce

###########################################################################
# Reactor

Session _ namedtuple('Session', ['address', 'file'])

sessions _ {}           # { csocket : Session(address, file)}
callback _ {}           # { csocket : callback(client, line) }
generators _ {}         # { csocket : inline callback generator }

# Main event loop
___ reactor(host, port):
    sock _ socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    sock.setblocking(0) # Make asynchronous

    sessions[sock] _ N..
    print(f'Server up, running, and waiting for call on {host} {port}')

    ___
        w__ T..:
            # Serve existing clients only if they already have data ready
            ready_to_read, _, _ _ select.select(sessions,    # list, [], 0.1)
            ___ conn __ ready_to_read:
                __ conn is sock:
                    conn, cli_address _ sock.accept()
                    connect(conn, cli_address)
                    c..

                line _ sessions[conn].file.readline()
                __ line:
                    callback[conn](conn, line.rstrip())
                ____
                    disconnect(conn)
    f..
        sock.close()

___ connect(conn, cli_address):
    sessions[conn] _ Session(cli_address, conn.makefile())

    gen _ process_request(conn)
    generators[conn] _ gen
    callback[conn] _ gen.send(N..) # Start the generator

___ disconnect(conn):
    gen _ generators.pop(conn)
    gen.close()
    sessions[conn].file.close()
    conn.close()

    del sessions[conn]
    del callback[conn]

@types.coroutine
___ readline(conn):
    ___ inner(conn, line):
        gen _ generators[conn]
        ___
            callback[conn] _ gen.send(line) # Continue the generator
        ______ StopIteration:
            disconnect(conn)

    line _ yield inner
    r_ line

###########################################################################
# User's Business Logic

? ___ process_request(conn):
    print(f'Received connection from {sessions[conn].address}')
    mode _ 'sum'

    ___
        conn.sendall(b'<welcome: starting in sum mode>\n')
        w__ T..:
            line _ ? readline(conn)
            __ line __ 'quit':
                conn.sendall(b'connection closed\r\n')
                r_
            __ line __ 'sum':
                conn.sendall(b'<switching to sum mode>\r\n')
                mode _ 'sum'
                c..
            __ line __ 'product':
                conn.sendall(b'<switching to product mode>\r\n')
                mode _ 'product'
                c..

            print(f'{sessions[conn].address} --> {line}')
            ___
                nums _ li..(m..(int, line.split(',')))
            ______ ValueError:
                conn.sendall(
                    b'ERROR. Enter only integers separated by commas\n')
                c..

            __ mode __ 'sum':
                conn.sendall(b'Sum of input integers: %a\r\n'
                    % st.(su.(nums)))
            ____
                conn.sendall(b'Product of input integers: %a\r\n'
                    % st.(reduce(mul, nums, 1)))
    f..
        print(f'{sessions[conn].address} quit')

__ _______ __ _______
    reactor('localhost', 8080)
