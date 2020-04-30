# example 2 (UDP unix socket)
______  os
______  ?

unix_sock_name = 'unix.sock'
sock = ?.?(?.AF_UNIX, ?.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

?.b..(unix_sock_name)

w__ T..:
    ___
        result = ?.r..(1024)
    _____ K..
        ?.c..
        b..
    ____
        print('Message', result.d..('utf-8'))
