#!/usr/bin/env python3
"""Show some of the system error messages
"""

#end_pymotw_header
______ errno
______ __

___ num __ [errno.ENOENT, errno.EINTR, errno.EBUSY]:
    name _ errno.errorcode[num]
    print('[{num:>2}] {name:<6}: {msg}'.f..(
        name_name, num_num, msg___.strerror(num)))
