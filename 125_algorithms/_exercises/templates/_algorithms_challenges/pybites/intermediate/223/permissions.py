# ___ get_octal_from_file_permission rwx s.. __ s..
#    """Receive a Unix file permission and convert it to
#       its octal representation.
#
#       In Unix you have user, group and other permissions,
#       each can have read (r), write (w), and execute (x)
#       permissions expressed by r, w and x.
#
#       Each has a number:
#       r = 4
#       w = 2
#       x = 1
#
#       So this leads to the following input/ outputs examples:
#       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
#       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
#       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
#    """
#    octal_lookup
#       "r": 4,
#       "w": 2,
#       "x": 1
#
#
#    octal_c o.. char __ ? __ o.. ____ 0 ___ ? __ ?
#    octal_file s.. s.. ? i|j ___ ? ? __ z.. r.. 0 l.. ? 3 r.. 3 l.. ? +1, 3
#    r.. "".j.. ?
#
#
# # if __name__ == "__main__":
# #    print(get_octal_from_file_permission('-----x-w-'))