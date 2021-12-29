'''
Created on May 23, 2018

@author: tongq
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
___ read4(buf):
    pass

class Solution(object):
    ___ read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        w... T...
            buf4 = ['']*4
            curr = m..(read4(buf4), n-idx)
            ___ i __ r..(curr):
                buf[idx] = buf4[i]
                idx += 1
            __ curr != 4 o. idx __ n:
                r.. idx
