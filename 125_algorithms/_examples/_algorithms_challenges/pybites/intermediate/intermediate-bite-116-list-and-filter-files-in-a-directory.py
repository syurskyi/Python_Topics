"""
In this Bite you complete get_files that receives a dirname and size_in_kb (note kb, not bytes).

There are two things you need to code:

Inspect/list the files in dirname,
Return files that are bigger or equal than size_in_kb (return a list or turn the function into a generator).
The os module is your friend here, but you also might want to check out glob. Have fun and keep coding in Python!
"""

# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
# https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python?noredirect=1&lq=1
# https://stackoverflow.com/questions/6591931/getting-file-size-in-python
# https://www.programiz.com/python-programming/methods/built-in/filter
# https://realpython.com/python-filter-function/
import os
import glob

ONE_KB = 1024

def get_files_implementation_1(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""

    # os.listdir return both directories and files, so it has to be filtered
    # list comprehension
    files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
    # list comprehension
    files_over_limit = [f for f in files if (os.path.getsize(os.path.join(dirname,f))) / ONE_KB >= size_in_kb]

    return files_over_limit

def get_files_implementation_2(dirname, size_in_kb):

    files_and_dirs = glob.glob("{dirname}/*".format(dirname=dirname))
    files = [f for f in files_and_dirs if os.path.isfile(f)]
    files_over_limit = [f for f in files if (os.path.getsize(f) / ONE_KB) >= size_in_kb]
    return files_over_limit

print(get_files_implementation_2("C:\\totalcmd", 5))
