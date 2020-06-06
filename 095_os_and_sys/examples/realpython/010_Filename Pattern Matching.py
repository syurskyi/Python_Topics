# Filename Pattern Matching
#
# After getting a list of files in a directory using one of the methods above, you will most probably want to search
# for files that match a particular pattern.
#
# These are the methods and functions available to you:
#
#     endswith() and startswith() string methods
#     fnmatch.fnmatch()
#     glob.glob()
#     pathlib.Path.glob()
#
# Each of these is discussed below. The examples in this section will be performed on a directory called some_directory
# that has the following structure:
#
# .
# |
# ├── sub_dir/
# |   ├── file1.py
# |   └── file2.py
# |
# ├── admin.py
# ├── data_01_backup.txt
# ├── data_01.txt
# ├── data_02_backup.txt
# ├── data_02.txt
# ├── data_03_backup.txt
# ├── data_03.txt
# └── tests.py
#
# If you’re following along using a Bash shell, you can create the above directory structure using the following
# commands:
#
# $ mkdir some_directory
# $ cd some_directory/
# $ mkdir sub_dir
# $ touch sub_dir/file1.py sub_dir/file2.py
# $ touch data_{01..03}.txt data_{01..03}_backup.txt admin.py tests.py
#
# This will create the some_directory/ directory, change into it, and then create sub_dir.
# The next line creates file1.py and file2.py in sub_dir, and the last line creates all the other files using expansion.
# To learn more about shell expansion, visit this site.