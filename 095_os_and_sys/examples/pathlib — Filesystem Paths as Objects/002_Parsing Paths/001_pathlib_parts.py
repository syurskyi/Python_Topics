# Path objects have methods and properties for extracting partial values from the name. For example, the parts property produces a sequence of path segments parsed based on the path separator value.
# pathlib_parts.py
#
# import pathlib
#
# p = pathlib.PurePosixPath('/usr/local')
# print(p.parts)
#
# The sequence is a tuple, reflecting the immutability of the path instance.
#
# $ python3 pathlib_parts.py
#
# ('/', 'usr', 'local')