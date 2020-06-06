# Let’s suppose you want to find .txt files that meet certain criteria. For example, you could be only interested
# in finding .txt files that contain the word data, a number between a set of underscores, and the word backup
# in their filename. Something similar to data_01_backup, data_02_backup, or data_03_backup.
#
# Using fnmatch.fnmatch(), you could do it this way:
#

import os
import fnmatch

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
        print(filename)

# Here, you print only the names of files that match the data_*_backup.txt pattern. The asterisk in the pattern
# will match any character, so running this will find all text files whose filenames start with the word data
# and end in backup.txt, as you can see from the output below:
#
# data_03_backup.txt
# data_02_backup.txt
# data_01_backup.txt

