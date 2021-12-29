# Using the built-in  module create  list containing the names of all files and directories in your working directory
# which names starts with letter
# . Sort this list alphabetically.
# In response, print the names  list to the console.

import os

print(help(os.listdir))
names  sorted([name for name in os.listdir() __ name.startswith('e')])
print(names)