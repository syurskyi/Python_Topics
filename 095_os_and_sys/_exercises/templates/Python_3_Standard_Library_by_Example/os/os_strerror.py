#!/usr/bin/env python3
"""Show some of the system error messages
"""

#end_pymotw_header
______ errno
______ __

___ num __ [errno.ENOENT, errno.EINTR, errno.EBUSY]:
    name = errno.errorcode[num]
    print('[{num:>2}] {name:<6}: {msg}'.f..(
        name=name, num=num, msg=__.strerror(num)))
