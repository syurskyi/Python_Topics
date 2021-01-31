# Where the .nuke folder lives in different directories
# ----- 01:44 -----
Linux = '/home/<your username>/.nuke'
Windows = 'C:\Users\<your username>\.nuke'
Mac = '/Users/<your username>/.nuke'




# Sublime, good text editor for coding
# ----- 03:48 -----

https://www.sublimetext.com/download
# I recommend the portable version, as some studios will let you use it...




# Adding new directories to init.py
# ----- 04:00 -----

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')




# Github link
# ----- 06:52 -----

# https://github.com


# Creating files & folders on Github
# ----- 08:39 -----


# Editing files on Github
# ----- 18:19 -----




# Importing modules
# ----- 13:45 -----

import nuke
import platform

# Python standard library: https://docs.python.org/3/library/




# Directory variables
# ----- 11:35 -----

import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\Ben\.nuke'
Mac_Dir = ''
Linux_Dir = '/home/benm/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = Mac_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None




# Finding help when you get stuck
# ----- 19:45 -----

# Lots of mistakes come from Syntax errors, indenting errors or misplaced characters.

# Google is your best friend.

# Nuke Developers Guide: https://learn.foundry.com/nuke/developers/63/ndkdevguide/