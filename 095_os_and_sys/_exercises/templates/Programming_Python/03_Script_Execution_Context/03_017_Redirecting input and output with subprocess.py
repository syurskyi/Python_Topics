# # C:\...\PP4E\System\Streams> python
# f___ subprocess ______ Popen, PIPE, call
# X = c... python hello-out.py # convenience
# # Hello shell world
# print ?
# # 0
# # ######################################################################################################################
#
# print('#' * 52)
# pipe _ Po.. python hello-out.py s.o. _ PI..
# print(?.com.. 0 # (s.o_, stderr)
# # b'Hello shell world\r\n'
# # ######################################################################################################################
#
# print ?.r.c. # exit status
# # 0
# # ######################################################################################################################
#
# pipe _ Po. python hello-out.py s.o_ _ PI..
# print ?.s.o_.r..
# # b'Hello shell world\r\n'
# # ######################################################################################################################
#
# print ?.wa.. # exit status
# # 0
# # ######################################################################################################################
#
# print('#' * 52)
# pipe _ Po.. python hello-in.py', s.i. _ PI..
# print ?.s.i_.w.. _'Pokey\n
# # 6
# # ######################################################################################################################
#
# ?.s.i_.cl..
# ?.wa..
# # 0
# # ######################################################################################################################
#
# print o... hello-in.txt .r.. # output sent to a file
# # 'Hello Pokey\n'
# # ######################################################################################################################
#
# print('#' * 52)
# # C:\...\PP4E\System\Streams> type writer.py
# # print("Help! Help! I'm being repressed!")
# # print(42)
# # C:\...\PP4E\System\Streams> type reader.py
# # print('Got this: "%s"' % input())
# ______ ___
# data _ ___.s.i_.r.l. :-1
# print('The meaning of life is', ? in.  ? * 2)
#
# print('#' * 52)
# pipe _ Po... python reader.py s.i. PI.. s.o__ PI..
# print(?.s.i_.w.. _'Lumberjack\n'))
# # 11
# # ######################################################################################################################
#
# ?.s.i_.w.. _'12\n
# # 3
# # ######################################################################################################################
#
# ?.s.i_.cl..
# output _ ?.s.o_.r..
# ?.wa..
# # 0
# # ######################################################################################################################
#
# print ?
# # b'Got this: "Lumberjack"\r\nThe meaning of life is 12 24\r\n'
#
# # C:\...\PP4E\System\Streams> python writer.py | python reader.py
# # Got this: "Help! Help! I'm being repressed!"
# # The meaning of life is 42 84
# # C:\...\PP4E\System\Streams> python
# # f___ subprocess ______ Popen, PIPE
# # p1 = Popen('python writer.py', s.o_=PIPE)
# # p2 = Popen('python reader.py', stdin=p1.s.o_, s.o_=PIPE)
# # output = p2.communicate()[0]
# # output
# # b'Got this: "Help! Help! I\'m being repressed!"\r\nThe meaning of life is 42 84\r\n'
# # p2.returncode
# # 0
#
# # ______ os
# # p1 = os.popen('python writer.py', 'r')
# # p2 = os.popen('python reader.py', 'w')
# # p2.write( p1.read() )
# # 36
# # X = p2.close()
# # Got this: "Help! Help! I'm being repressed!"
# # The meaning of life is 42 84
# # print(X)
# # None