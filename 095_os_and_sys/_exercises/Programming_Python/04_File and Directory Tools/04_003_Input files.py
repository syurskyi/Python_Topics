# C:\temp> python
file = open('data.txt')  # open input file object: 'r' default
lines = file.readlines()  # read into line string list
for line in lines:  # BUT use file line iterator! (ahead)
    print(line, end='')  # lines have a '\n' at end

# Hello file world!
# Bye file world.

file.seek(0)  # go back to the front of file
file.read()  # read entire file into string
# 'Hello file world!\nBye file world.\n'
# ######################################################################################################################

file.seek(0)  # read entire file into lines list
file.readlines()
# ['Hello file world!\n', 'Bye file world.\n']
# ######################################################################################################################

file.seek(0)
file.readline()  # read one line at a time
# 'Hello file world!\n'
# ######################################################################################################################

file.readline()
# 'Bye file world.\n'
# ######################################################################################################################

file.readline()  # empty string at end-of-file
# ''
# ######################################################################################################################

file.seek(0)  # read N (or remaining) chars/bytes
file.read(1), file.read(8)  # empty string at end-of-file
# ('H', 'ello fil')
# ######################################################################################################################