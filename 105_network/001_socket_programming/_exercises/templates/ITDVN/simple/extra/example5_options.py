______  ?

sock = ?.?(?.A_I.., ?.SOCK_DGRAM)
# 255.255.255.255
?.b..(('127.0.0.1', 8888))
?.l..(5)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
?.setsockopt(?.SOL_SOCKET, ?.SO_REUSEADDR, 1)


client, addr = ?.a..
result = client.r..(1024)
client.c..

print('Message', result.d..('utf-8'))
