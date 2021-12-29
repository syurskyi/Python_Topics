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
        __ ':' in IP and self.checkIP6(IP):
            return 'IPv6'
        elif '.' in IP and self.checkIP4(IP):
            return 'IPv4'
        return 'Neither'
    
    ___ checkIP4(self, ip):
        arr = ip.split('.')
        __ len(arr) != 4: return False
        for elem in arr:
            __ not elem: return False
            __ elem.startswith('0') and len(elem) > 1: return False
            __ not elem.isdigit() or int(elem) > 255:
                return False
        return True
    
    ___ checkIP6(self, ip):
        arr = ip.split(':')
        __ len(arr) != 8: return False
        digits = set(list('0123456789abcdefABCDEF'))
        for i, elem in enumerate(arr):
            __ i > 0 and len(elem) > 4: return False
            __ i == 0 and len(elem) > 4:
                __ elem[:len(elem)-4] != '0'*(len(elem)-4):
                    return False
            __ not elem: return False
            for c in elem:
                __ c not in digits:
                    return False
        return True
