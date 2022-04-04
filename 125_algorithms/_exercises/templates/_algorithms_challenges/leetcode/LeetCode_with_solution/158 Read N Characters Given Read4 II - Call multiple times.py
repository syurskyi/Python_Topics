"""
Premium Question
"""
__author__ = 'Daniel'


___ read4(buf
    """
    read 4 chars to buf

    :type buf: List[str]
    :rtype: int
    """
    r.. 0


c_ Solution(o..
    ___ -
        prev    # list

    ___ read  buf, n
        """
        read n chars to buf, called multiple times

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        l = m..(l..(prev), n)
        buf[:l] = prev[:l]
        prev = prev[l:]  # pitfall self.prev = []

        idx = l  # the next reading
        w.... idx < n:
            buf4 = ["" ___ _ __ x..(4)]
            r = read4(buf4)
            __ idx+r < n:
                buf[idx:idx+r] = buf4[:r]
                idx += r
                __ r < 4: r.. idx
            ____
                buf[idx:n] = buf4[:n-idx]
                prev = buf4[n-idx:r]  # pitfall buf4[n-idx:]
                idx = n

        r.. idx