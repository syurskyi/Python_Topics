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

names = ['John', 'Joshua', '1tim', 'Al', 'Benjamin', 'Franklin', 'George', 'Nagendra', '1tim']

# Solution #1
def filter_names_1(names):
    filtered = []
    cnt = 0
    for name in names:
        if name.lower()[0] == IGNORE_CHAR or not name.isalpha():
            continue
        if name.lower()[0] == QUIT_CHAR:
            break
        if cnt < 5:
            filtered.append(name)
        else:
            break
        cnt += 1
    return filtered

print(filter_names_1(names))

# Solution 2 (using generator)
def filter_names_2(names):
    cnt = 0
    for name in names:
        if name.lower()[0] == IGNORE_CHAR or not name.isalpha():
            continue
        if name.lower()[0] == QUIT_CHAR:
            break
        if cnt < 5:
            cnt += 1
            yield name
        else:
            break