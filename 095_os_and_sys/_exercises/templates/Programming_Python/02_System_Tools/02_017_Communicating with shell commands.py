import os
print(open('helloshell.py').read())

text = os.popen('type helloshell.py').read()
print(text)
# "# a Python program\nprint('The Meaning of Life')\n"
# ######################################################################################################################

print('#' * 52)
listing = os.popen('dir /B').readlines()
print(listing)
# ['helloshell.py\n', 'more.py\n', 'more.pyc\n', 'spam.txt\n', '__init__.py\n']
# ######################################################################################################################

print('#' * 52)
os.system('python helloshell.py') # run a Python program
# The Meaning of Life
# 0
# ######################################################################################################################

output = os.popen('python helloshell.py').read()
print(output)
# 'The Meaning of Life\n'
# ######################################################################################################################