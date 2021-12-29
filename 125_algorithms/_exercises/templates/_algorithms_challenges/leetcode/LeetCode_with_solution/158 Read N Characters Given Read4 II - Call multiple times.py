"""
Premium Question
"""
__author__ = 'Daniel'


___ read4(buf):
    """
    read 4 chars to buf

    :type buf: List[str]
    :rtype: int
    """
    return 0


class Solution(object):
    ___ __init__(self):
        self.prev = []

    ___ read(self, buf, n):
        """
        read n chars to buf, called multiple times

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        l = min(len(self.prev), n)
        buf[:l] = self.prev[:l]
        self.prev = self.prev[l:]  # pitfall self.prev = []

        idx = l  # the next reading
        while idx < n:
            buf4 = ["" for _ in xrange(4)]
            r = read4(buf4)
            __ idx+r < n:
                buf[idx:idx+r] = buf4[:r]
                idx += r
                __ r < 4: return idx
            else:
                buf[idx:n] = buf4[:n-idx]
                self.prev = buf4[n-idx:r]  # pitfall buf4[n-idx:]
                idx = n

        return idx