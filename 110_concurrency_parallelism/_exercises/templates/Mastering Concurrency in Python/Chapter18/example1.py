# ch18/example1.py

______ socket

# Main event loop
___ reactor(host, port):
    sock _ socket.socket()
    sock.bind((host, port))
    sock.listen(5)
    print(f'Server up, running, and waiting for call on {host} {port}')

    ___
        w__ T..:
            conn, cli_address _ sock.accept()
            process_request(conn, cli_address)

    f..
        sock.close()

___ process_request(conn, cli_address):
    file _ conn.makefile()

    print(f'Received connection from {cli_address}')

    ___
        w__ T..:
            line _ file.readline()
            __ line:
                line _ line.rstrip()
                __ line __ 'quit':
                    conn.sendall(b'connection closed\r\n')
                    r_

                print(f'{cli_address} --> {line}')
                conn.sendall(b'Echoed: %a\r\n' % line)
    f..
        print(f'{cli_address} quit')
        file.close()
        conn.close()

__ _______ __ _______
    reactor('localhost', 8080)
