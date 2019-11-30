import os
for line in os.popen('dir /B *.py'): print(line, end='')

# helloshell.py
# more.py
# __init__.py

print('#' * 52)
I = os.popen('dir /B *.py')
print(I)
# <os._wrap_close object at 0x013BC750>
# ######################################################################################################################

print('#' * 52)
I = os.popen('dir /B *.py')
print(I.__next__())
print(I.__next__())
# 'helloshell.py\n'
# I = os.popen('dir /B *.py')
# next(I)
# TypeError: _wrap_close object is not an iterator
# ######################################################################################################################

print('#' * 52)
I = os.popen('dir /B *.py')
I = iter(I) # what for loops do
print(I.__next__())  # now both forms work
# 'helloshell.py\n'
# next(I)
# 'more.py\n'
# ######################################################################################################################