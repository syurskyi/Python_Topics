# ______ s......
#
# sock _ s____.s____(s____.AF_INET, s____.SOCK_STREAM)
# s___.b____ '127.0.0.1' 8888
# s___.l_____ 5
# # s___.s..b... T...
# # s___.s..t.... 5
# # s___.s..t... 0  # ->  sock.blocking(False)
# s___.s..t... N...  # ->  sock.blocking(True)
#
# t..
#     client, addr _ s___.a_____
# e___ s____.e...
#     print No connections
# # except socket.timeout:
# #     print('timed out')
# e____
#     result _ cl__.r... 1024
#     c___.cl...
#     print 'Message' r____.d... utf-8
