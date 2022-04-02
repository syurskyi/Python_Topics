'''
Created on Apr 25, 2017

@author: MT
'''

c_ Solution(o..
    ___ validIPAddress  IP
        """
        :type IP: str
        :rtype: str
        """
        __ ':' __ IP a.. checkIP6(IP
            r.. 'IPv6'
        ____ '.' __ IP a.. checkIP4(IP
            r.. 'IPv4'
        r.. 'Neither'
    
    ___ checkIP4  ip
        arr = ip.s..('.')
        __ l..(arr) != 4: r.. F..
        ___ elem __ arr:
            __ n.. elem: r.. F..
            __ elem.startswith('0') a.. l..(elem) > 1: r.. F..
            __ n.. elem.i.. o. i..(elem) > 255:
                r.. F..
        r.. T..
    
    ___ checkIP6  ip
        arr = ip.s..(':')
        __ l..(arr) != 8: r.. F..
        d.. = s..(l..('0123456789abcdefABCDEF'))
        ___ i, elem __ e..(arr
            __ i > 0 a.. l..(elem) > 4: r.. F..
            __ i __ 0 a.. l..(elem) > 4:
                __ elem[:l..(elem)-4] != '0'*(l..(elem)-4
                    r.. F..
            __ n.. elem: r.. F..
            ___ c __ elem:
                __ c n.. __ d..:
                    r.. F..
        r.. T..
