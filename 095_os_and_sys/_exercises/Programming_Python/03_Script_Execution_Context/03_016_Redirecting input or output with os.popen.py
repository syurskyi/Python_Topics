# C:\...\PP4E\System\Streams> type hello-out.py
# print('Hello shell world')
# C:\...\PP4E\System\Streams> type hello-in.py
# inp = input()
# open('hello-in.txt', 'w').write('Hello ' + inp + '\n')

# C:\...\PP4E\System\Streams> python hello-out.py
# Hello shell world
# C:\...\PP4E\System\Streams> python hello-in.py
# Brian
# C:\...\PP4E\System\Streams> type hello-in.txt
# Hello Brian
#
# C:\...\PP4E\System\Streams> python
import os
pipe = os.popen('python hello-out.py') # 'r' is default--read stdout
print(pipe.read())
# 'Hello shell world\n'
# ######################################################################################################################

print(pipe.close()) # exit status: None is good
# None

pipe = os.popen('python hello-in.py', 'w') # 'w'--write to program stdin
pipe.write('Gumby\n')
# 6
# pipe.close() # \n at end is optional
print(open('hello-in.txt').read()) # output sent to a file
# 'Hello Gumby\n'
