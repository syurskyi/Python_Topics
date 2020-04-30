# with operator
______  ?

# __enter__ / __exit__
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with ?.?(?.A_I.., ?.SOCK_DGRAM) as sock:
    print('8888 is bind')
    ?.b..(('127.0.0.1', 8888))

    while True:
        result = ?.r..(1024)
        print('Message', result.d..('utf-8'))
