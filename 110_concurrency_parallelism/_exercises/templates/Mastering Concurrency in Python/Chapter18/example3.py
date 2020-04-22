# ch18/example3.py

______ socket
____ operator ______ mul
____ functools ______ reduce

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
    mode _ 'sum'

    ___
        conn.sendall(b'<welcome: starting in sum mode>\n')
        w__ T..:
            line _ file.readline()
            __ line:
                line _ line.rstrip()
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

                print(f'{cli_address} --> {line}')
                ___
                    nums _ li..(m..(int, line.split(',')))
                ______ ValueError:
                    conn.sendall(
                        b'ERROR. Enter only integers separated by commas\n')
                    c..

                __ mode __ 'sum':
                    conn.sendall(b'Sum of input numbers: %a\r\n'
                        % st.(su.(nums)))
                ____
                    conn.sendall(b'Product of input numbers: %a\r\n'
                        % st.(reduce(mul, nums, 1)))
    f..
        print(f'{cli_address} quit')
        file.close()
        conn.close()

__ _______ __ _______
    reactor('localhost', 8080)
