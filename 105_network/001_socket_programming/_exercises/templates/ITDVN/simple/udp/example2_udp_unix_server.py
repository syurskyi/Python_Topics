# example 2 (UDP unix socket)
______  os
______  ?

unix_sock_name = 'unix.sock'
sock = ?.?(?.AF_UNIX, ?.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

?.b..(unix_sock_name)

while True:
    try:
        result = ?.r..(1024)
    except KeyboardInterrupt:
        ?.c..
        break
    else:
        print('Message', result.d..('utf-8'))
