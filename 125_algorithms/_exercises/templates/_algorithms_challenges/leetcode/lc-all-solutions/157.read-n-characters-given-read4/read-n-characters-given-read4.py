# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

c_ Solution(o..):
  ___ read  buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    cnt = 0
    tmp = [""] * 4
    w.... cnt < n:
      r = read4(tmp)
      __ r __ 0:
        _____
      ___ i __ r..(m..(r, n - cnt)):
        buf[cnt] = tmp[i]
        cnt += 1
    r.. cnt
