'''
Created on Apr 25, 2017

@author: MT
'''

class Solution(object
    ___ validIPAddress(self, IP
        """
        :type IP: str
        :rtype: str
        """
        __ ':' in IP and self.checkIP6(IP
            r_ 'IPv6'
        ____ '.' in IP and self.checkIP4(IP
            r_ 'IPv4'
        r_ 'Neither'
    
    ___ checkIP4(self, ip
        arr = ip.split('.')
        __ le.(arr) != 4: r_ False
        for elem in arr:
            __ not elem: r_ False
            __ elem.startswith('0') and le.(elem) > 1: r_ False
            __ not elem.isdigit() or int(elem) > 255:
                r_ False
        r_ True
    
    ___ checkIP6(self, ip
        arr = ip.split(':')
        __ le.(arr) != 8: r_ False
        digits = set(list('0123456789abcdefABCDEF'))
        for i, elem in enumerate(arr
            __ i > 0 and le.(elem) > 4: r_ False
            __ i __ 0 and le.(elem) > 4:
                __ elem[:le.(elem)-4] != '0'*(le.(elem)-4
                    r_ False
            __ not elem: r_ False
            for c in elem:
                __ c not in digits:
                    r_ False
        r_ True
