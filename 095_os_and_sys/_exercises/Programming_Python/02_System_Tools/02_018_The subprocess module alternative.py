import subprocess
print('#' * 52 + 'roughly like os.system()')
subprocess.call('python helloshell.py') # roughly like os.system()
# The Meaning of Life
# 0
# ######################################################################################################################

print('#' * 52 + 'built-in shell cmd')
subprocess.call('cmd /C "type helloshell.py"') # built-in shell cmd
# a Python program
# print('The Meaning of Life')
# 0
# ######################################################################################################################

print('#' * 52 + 'alternative for built-ins')
subprocess.call('type helloshell.py', shell=True) # alternative for built-ins
# a Python program
# print('The Meaning of Life')
# 0
# ######################################################################################################################

print('#' * 52)
pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
print(pipe.communicate())
# (b'The Meaning of Life\r\n', None)
print(pipe.returncode)
# 0
# ######################################################################################################################

print('#' * 52)
pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
print(pipe.stdout.read())
# b'The Meaning of Life\r\n'
# pipe.wait()
# 0
# ######################################################################################################################

print('#' * 52)
from subprocess import Popen, PIPE
print(Popen('python helloshell.py', stdout=PIPE).communicate()[0])
# b'The Meaning of Life\r\n'
# ######################################################################################################################

print('#' * 52)
import os
print(os.popen('python helloshell.py').read())
# 'The Meaning of Life\n'
# ######################################################################################################################