'''
Here is a Bite to practice the continue and break statements in Python.

Complete filter_names that takes a list of names and returns a filtered list (or generator) of names using the
following conditions:

names that start with IGNORE_CHAR are ignored,
names that have one or more digits are ignored,
if a name starts with QUIT_CHAR it inmediately exits the loop, so no more names are added/generated
at this point (neither the QUIT_CHAR name),
return up till MAX_NAMES names max.
'''

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5

names =  'John', 'Joshua', '1tim', 'Al', 'Benjamin', 'Franklin', 'George', 'Nagendra', '1tim'

# Solution #1
___ filter_names_1(names
    filtered    # list
    cnt = 0
    ___ name __ names:
        __ name.l..[0] __ IGNORE_CHAR o. n.. name.isalpha
            _____
        __ name.l..[0] __ QUIT_CHAR:
            _____
        __ cnt < 5:
            filtered.a..(name)
        ____:
            _____
        cnt += 1
    r.. filtered

print(filter_names_1(names

# Solution 2 (using generator)
___ filter_names_2(names
    cnt = 0
    ___ name __ names:
        __ name.l..[0] __ IGNORE_CHAR o. n.. name.isalpha
            _____
        __ name.l..[0] __ QUIT_CHAR:
            _____
        __ cnt < 5:
            cnt += 1
            y.. name
        ____:
            _____