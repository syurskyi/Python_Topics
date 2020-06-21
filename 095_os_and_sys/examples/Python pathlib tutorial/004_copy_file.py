#!/usr/bin/env python

from pathlib import Path
from shutil import copyfile

source = Path('words.txt')
destination = Path('words_bck.txt')

copyfile(source, destination)

#  The example makes a copy of a words.txt file.
#
# source = Path('words.txt')
#
# A file object is created by passing the file name to the Path constructor. 