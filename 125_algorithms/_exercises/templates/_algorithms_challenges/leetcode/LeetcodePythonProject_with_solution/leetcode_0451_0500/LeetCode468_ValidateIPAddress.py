'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object):
    ___ validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        __ ':' __ IP and self.checkIP6(IP):
            r.. 'IPv6'
        ____ '.' __ IP and self.checkIP4(IP):
            r.. 'IPv4'
        r.. 'Neither'
    
    ___ checkIP4(self, ip):
        arr = ip.split('.')
        __ l..(arr) != 4: r.. False
        ___ elem __ arr:
            __ n.. elem: r.. False
            __ elem.startswith('0') and l..(elem) > 1: r.. False
            __ n.. elem.isdigit() o. int(elem) > 255:
                r.. False
        r.. True
    
    ___ checkIP6(self, ip):
        arr = ip.split(':')
        __ l..(arr) != 8: r.. False
        digits = set(l..('0123456789abcdefABCDEF'))
        ___ i, elem __ enumerate(arr):
            __ i > 0 and l..(elem) > 4: r.. False
            __ i __ 0 and l..(elem) > 4:
                __ elem[:l..(elem)-4] != '0'*(l..(elem)-4):
                    r.. False
            __ n.. elem: r.. False
            ___ c __ elem:
                __ c n.. __ digits:
                    r.. False
        r.. True
