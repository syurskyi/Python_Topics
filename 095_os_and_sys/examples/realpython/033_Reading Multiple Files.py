# Python supports reading data from multiple input streams or from a list of files through the fileinput module.
# This module allows you to loop over the contents of one or more text files quickly and easily. Here’s the typical
# way fileinput is used:
#
# import fileinput
# for line in fileinput.input()
#     process(line)
#
# fileinput gets its input from command line arguments passed to sys.argv by default.
#
# Using fileinput to Loop Over Multiple Files
#
# Let’s use fileinput to build a crude version of the common UNIX utility cat. The cat utility reads files sequentially,
# writing them to standard output. When given more than one file in its command line arguments,
# cat will concatenate the text files and display the result in the terminal:
#
# # File: fileinput-example.py
# import fileinput
# import sys
#
# files = fileinput.input()
# for line in files:
#     if fileinput.isfirstline():
#         print(f'\n--- Reading {fileinput.filename()} ---')
#     print(' -> ' + line, end='')
# print()
#
# Running this on two text files in my current directory produces the following output:
#
# $ python3 fileinput-example.py bacon.txt cupcake.txt
# --- Reading bacon.txt ---
#  -> Spicy jalapeno bacon ipsum dolor amet in in aute est qui enim aliquip,
#  -> irure cillum drumstick elit.
#  -> Doner jowl shank ea exercitation landjaeger incididunt ut porchetta.
#  -> Tenderloin bacon aliquip cupidatat chicken chuck quis anim et swine.
#  -> Tri-tip doner kevin cillum ham veniam cow hamburger.
#  -> Turkey pork loin cupidatat filet mignon capicola brisket cupim ad in.
#  -> Ball tip dolor do magna laboris nisi pancetta nostrud doner.
#
# --- Reading cupcake.txt ---
#  -> Cupcake ipsum dolor sit amet candy I love cheesecake fruitcake.
#  -> Topping muffin cotton candy.
#  -> Gummies macaroon jujubes jelly beans marzipan.
#
# fileinput allows you to retrieve more information about each line such as whether or not it is the first line
# (.isfirstline()), the line number (.lineno()), and the filename (.filename()). You can read more about it here.
# Conclusion
#
# You now know how to use Python to perform the most common operations on files and groups of files.
# You’ve learned about the different built-in modules used to read, find, and manipulate them.
#
# You’re now equipped to use Python to:
#
#     Get directory contents and file properties
#     Create directories and directory trees
#     Find patterns in filenames
#     Create temporary files and directories
#     Move, rename, copy, and delete files or directories
#     Read and extract data from different types of archives
#     Read multiple files simultaneously using fileinput