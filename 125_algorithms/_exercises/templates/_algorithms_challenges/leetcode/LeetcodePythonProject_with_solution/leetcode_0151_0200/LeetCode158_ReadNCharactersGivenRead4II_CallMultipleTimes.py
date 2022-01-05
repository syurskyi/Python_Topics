'''
Created on May 23, 2018

@author: tongq
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
___ read4(buf):
    p..

c_ Solution(object):
    ___ - ):
        queue    # list
    
    ___ read  buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        w... T...
            buf4 = ['']*4
            read4(buf4)
            queue.extend(buf4)
            curr = m..(l..(queue), n-idx)
            ___ _ __ r..(curr):
                buf[idx] = queue.pop(0)
                idx += 1
            __ curr __ 0:
                break
        r.. idx
