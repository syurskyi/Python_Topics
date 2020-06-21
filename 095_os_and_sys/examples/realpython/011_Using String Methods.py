# Python has several built-in methods for modifying and manipulating strings. Two of these methods, .startswith()
# and .endswith(), are useful when you’re searching for patterns in filenames. To do this, first get a directory listing
# and then iterate over it:

import os

# Get .txt files
for f_name in os.listdir('some_directory'):
    if f_name.endswith('.txt'):
        print(f_name)

# The code above finds all the files in some_directory/, iterates over them and uses .endswith() to print out
# the filenames that have the .txt file extension. Running this on my computer produces the following output:
#
# data_01.txt
# data_03.txt
# data_03_backup.txt
# data_02_backup.txt
# data_02.txt
# data_01_backup.txt

