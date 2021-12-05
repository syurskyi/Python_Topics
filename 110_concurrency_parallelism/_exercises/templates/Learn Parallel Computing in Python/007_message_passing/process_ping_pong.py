from _ ______ P.., Pipe

______ time


___ ping(pipe_conn):
    while (True):
        pipe_conn.send(["Ping", time.time()])
        pong = pipe_conn.recv()
        print(pong)
        time.sleep(1)


___ pong(pipe_conn):
    while (True):
        ping = pipe_conn.recv()
        print(ping)
        time.sleep(1)
        pipe_conn.send(["Pong", time.time()])


__ _____ __ _____
    pipe_end_a, pipe_end_b = Pipe()
    P..(t.._ping, a.._(pipe_end_a,)).start()
    P..(t.._pong, a.._(pipe_end_b,)).start()
