____ _ ______ P.., Pipe

______ t___


___ ping(pipe_conn):
    w... (True):
        pipe_conn.send(["Ping", t___.t___()])
        pong = pipe_conn.recv()
        print(pong)
        t___.s..(1)


___ pong(pipe_conn):
    w... (True):
        ping = pipe_conn.recv()
        print(ping)
        t___.s..(1)
        pipe_conn.send(["Pong", t___.t___()])


__ _____ __ _____
    pipe_end_a, pipe_end_b = Pipe()
    P..(t.._ping, a.._(pipe_end_a,)).s..
    P..(t.._pong, a.._(pipe_end_b,)).s..
