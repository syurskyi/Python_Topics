# # String methods are limited in their matching abilities. fnmatch has more advanced functions and methods
# # for pattern matching. We will consider fnmatch.fnmatch(), a function that supports the use of wildcards
# # such as * and ? to match filenames. For example, in order to find all .txt files in a directory using fnmatch,
# # you would do the following:
#
# ______ __
# ______ f_m_
#
# ___ file_name __ __.l_d_ 'some_directory/'
#     __ f_m_.f_m_ ? '@.txt'
#         print ?
#
# # This iterates over the list of files in some_directory and uses .fnmatch() to perform a wildcard search
# # for files that have the .txt extension.