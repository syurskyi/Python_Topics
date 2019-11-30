import os
print(os.environ['TEMP'])
# 'C:\\Users\\mark\\AppData\\Local\\Temp
os.environ['TEMP'] = r'c:\temp'
print(os.environ['TEMP'])
# 'c:\\temp'

# in the shell itself:
# C:\...\PP4E\System\Environment> set USER=Bob
# C:\...\PP4E\System\Environment> python echoenv.py
# echoenv... Hello, Bob
# ######################################################################################################################

print('#' * 52 + 'setenv.py')
import os
print('setenv...', end=' ')
print(os.environ['USER'])                # show current shell variable value
#
# os.environ['USER'] = 'Brian'             # runs os.putenv behind the scenes
# os.system('python echoenv.py')
#
# os.environ['USER'] = 'Arthur'            # changes passed to spawned programs
# os.system('python echoenv.py')           # and linked-in C library modules
#
# os.environ['USER'] = input('?')
# print(os.popen('python echoenv.py').read())
#
# C:\...\PP4E\System\Environment> python setenv.py
# setenv... Bob
# echoenv... Hello, Brian
# echoenv... Hello, Arthur
# ?Gumby
# echoenv... Hello, Gumby
# C:\...\PP4E\System\Environment> echo %USER%
# Bob
# ######################################################################################################################