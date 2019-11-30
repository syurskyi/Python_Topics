file = open('data.txt')
for line in file.readlines(): # DON'T DO THIS ANYMORE!
    print(line, end='')

file = open('data.txt')
for line in file: # no need to call readlines
    print(line, end='') # iterator reads next line each time

# Hello file world!
# Bye file world.
# ######################################################################################################################

for line in open('data.txt'): # even shorter: temporary file object
    print(line, end='') # auto-closed when garbage collected

# Hello file world!
# Bye file world.
# ######################################################################################################################

file = open('data.txt') # read methods: empty at EOF
file.readline()
# 'Hello file world!\n'
# ######################################################################################################################

file.readline()
# 'Bye file world.\n'
# ######################################################################################################################

file.readline()
# ''
# ######################################################################################################################
file = open('data.txt') # iterators: exception at EOF
file.__next__() # no need to call iter(file) first,
# 'Hello file world!\n' # since files are their own iterator
# ######################################################################################################################

file.__next__()
# 'Bye file world.\n'
# ######################################################################################################################

file.__next__()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# StopIteration
# ######################################################################################################################

open('data.txt').readlines() # always read lines
# ['Hello file world!\n', 'Bye file world.\n']
# ######################################################################################################################

list(open('data.txt')) # force line iteration
# ['Hello file world!\n', 'Bye file world.\n']
# ######################################################################################################################

lines = [line.rstrip() for line in open('data.txt')] # comprehension
lines
# ['Hello file world!', 'Bye file world.']
# ######################################################################################################################

lines = [line.upper() for line in open('data.txt')] # arbitrary actions
lines
# ['HELLO FILE WORLD!\n', 'BYE FILE WORLD.\n']
# ######################################################################################################################

list(map(str.split, open('data.txt'))) # apply a function
# [['Hello', 'file', 'world!'], ['Bye', 'file', 'world.']]
# ######################################################################################################################

line = 'Hello file world!\n'
line in open('data.txt') # line membership
# True
# ######################################################################################################################
