___ get_octal_from_file_permission(rwx: s..) __ s..
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """

    base =2 
    number    # list
    ___ i __ r..(0,l..(rwx),3
        permissions rwx[i:i+3]
        r 0
        ___ i,value __ e..(r..(permissions:
            __ value !_ '-':
                r += base**(i)



        number.a..(s..(r


    r.. ''.j..(number)












