# example 3 (TCP server socket)
______  ?

sock = ?.?(?.A_I.., ?.S_S..)
?.b..(('127.0.0.1', 8888))
?.l..(5)

while True:
    try:
        client, addr = ?.a..
    except KeyboardInterrupt:
        ?.c..
        break
    else:
        result = client.r..(1024)
        client.c..
        print('Message', result.d..('utf-8'))
