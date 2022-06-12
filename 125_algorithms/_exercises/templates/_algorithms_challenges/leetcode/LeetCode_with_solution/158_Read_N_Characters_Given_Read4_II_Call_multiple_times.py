# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

c_ Solution o..

    ___ - ____:
        buff = [''] * 4
        offset = 0
        bufsize = 0

    ___ read  buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        pos, eof = 0, False
        w.. not eof and pos < n:
            __ bufsize __ 0:
                bufsize = read4(buff)
                eof = bufsize < 4
            byte = min(n - pos, bufsize)
            ___ i __ r.. byte):
                buf[pos + i] = buff[offset + i]
            offset = (offset + byte) % 4
            bufsize -= byte
            pos += byte
        r_ pos
