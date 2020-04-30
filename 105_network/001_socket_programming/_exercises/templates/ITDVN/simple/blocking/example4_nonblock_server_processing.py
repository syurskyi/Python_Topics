______  ?

sock = ?.?(?.A_I.., ?.S_S..)
?.b..(('127.0.0.1', 8888))
?.l..(5)
?.s..(F..)

while True:
    try:
        client, addr = ?.a..
    except ?.error:
        print('no clients')
    except KeyboardInterrupt:
        break
    else:
        client.s..(True)
        result = client.r..(1024)
        client.c..
        print('Message', result.d..('utf-8'))
