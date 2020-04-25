

______ so..

size _ 512
host _ ''
port _ 9898
#  family = Internet, type = stream socket means TCP
sock _ ?.?(?.A.. ?.S..
sock.s_s_(?.S_S.., ?.S_R.., 1)
#  we have a socket, we need to bind to an IP address and port
#  to have a place to listen on
sock.b..((host, port))
sock.l..(5)
#  we can store information about the other end
#  once we accept the connection attempt
c, addr _ sock.a..
data _ c.r..(size)
__ data:
    f _ o..("storage.dat", '+w')
    print("connection from: ", addr[0])
    f.w..(addr[0])
    f.w..(":")
    f.w..(data.d..("utf-8"))
    f.c..
sock.c..





