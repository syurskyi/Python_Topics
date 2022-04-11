"""
Premium Question
"""
__author__ 'Daniel'


___ read4(buf
    """
    read 4 chars to buf

    :type buf: List[str]
    :rtype: int
    """
    r.. 0


c_ Solution(o..
    ___ read  buf, n
        """
        read n chars to buf
        Algorithm:
        Two dimensions
          1st dim: buf full or not
          2nd dim: buf4 full or not

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx 0
        w.... idx < n:
            buf4 ["" ___ _ __ x..(4)]
            r read4(buf4)
            __ idx+r < n:
                buf[idx:idx+r] buf4[:r]
                idx += r
                __ r < 4: _____
            ____
                buf[idx:n] buf4 |?-idx]
                idx n

        r.. idx
