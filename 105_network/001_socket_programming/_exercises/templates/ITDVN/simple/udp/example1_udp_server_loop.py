# example 1 (UDP server socket)
______  ?

sock = ?.?(?.A_I.., ?.SOCK_DGRAM)
?.b..(('127.0.0.1', 8888))

while True:
    try:
        result = ?.r..(1024)
    except KeyboardInterrupt:
        ?.c..
        break
    else:
        print('Message', result.d..('utf-8'))
