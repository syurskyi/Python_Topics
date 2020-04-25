______ so..

HOST _ '127.0.0.1'  # Standard loopback interface address (localhost)
PORT _ 8081        # Port to listen on (non-privileged ports are > 1023)

w__ ?.?(?.A.. ?.S.. __ s:
    s.b..((HOST, PORT))
    s.l..
    conn, addr _ s.a..
    w__ conn:
        print('Connected by', addr)
        w__ T..:
            data _ conn.r..(1024)
            __ not data:
                b..
            conn.s_a..(data)