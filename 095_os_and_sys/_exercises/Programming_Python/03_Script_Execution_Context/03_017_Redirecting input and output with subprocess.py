# C:\...\PP4E\System\Streams> python
from subprocess import Popen, PIPE, call
X = call('python hello-out.py') # convenience
# Hello shell world
print(X)
# 0
# ######################################################################################################################

print('#' * 52)
pipe = Popen('python hello-out.py', stdout=PIPE)
print(pipe.communicate()[0]) # (stdout, stderr)
# b'Hello shell world\r\n'
# ######################################################################################################################

print(pipe.returncode) # exit status
# 0
# ######################################################################################################################

pipe = Popen('python hello-out.py', stdout=PIPE)
print(pipe.stdout.read())
# b'Hello shell world\r\n'
# ######################################################################################################################

print(pipe.wait()) # exit status
# 0
# ######################################################################################################################

print('#' * 52)
pipe = Popen('python hello-in.py', stdin=PIPE)
print(pipe.stdin.write(b'Pokey\n'))
# 6
# ######################################################################################################################

pipe.stdin.close()
pipe.wait()
# 0
# ######################################################################################################################

print(open('hello-in.txt').read()) # output sent to a file
# 'Hello Pokey\n'
# ######################################################################################################################

print('#' * 52)
# C:\...\PP4E\System\Streams> type writer.py
# print("Help! Help! I'm being repressed!")
# print(42)
# C:\...\PP4E\System\Streams> type reader.py
# print('Got this: "%s"' % input())
import sys
data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data) * 2)

print('#' * 52)
pipe = Popen('python reader.py', stdin=PIPE, stdout=PIPE)
print(pipe.stdin.write(b'Lumberjack\n'))
# 11
# ######################################################################################################################

pipe.stdin.write(b'12\n')
# 3
# ######################################################################################################################

pipe.stdin.close()
output = pipe.stdout.read()
pipe.wait()
# 0
# ######################################################################################################################

print(output)
# b'Got this: "Lumberjack"\r\nThe meaning of life is 12 24\r\n'

# C:\...\PP4E\System\Streams> python writer.py | python reader.py
# Got this: "Help! Help! I'm being repressed!"
# The meaning of life is 42 84
# C:\...\PP4E\System\Streams> python
# from subprocess import Popen, PIPE
# p1 = Popen('python writer.py', stdout=PIPE)
# p2 = Popen('python reader.py', stdin=p1.stdout, stdout=PIPE)
# output = p2.communicate()[0]
# output
# b'Got this: "Help! Help! I\'m being repressed!"\r\nThe meaning of life is 42 84\r\n'
# p2.returncode
# 0

# import os
# p1 = os.popen('python writer.py', 'r')
# p2 = os.popen('python reader.py', 'w')
# p2.write( p1.read() )
# 36
# X = p2.close()
# Got this: "Help! Help! I'm being repressed!"
# The meaning of life is 42 84
# print(X)
# None