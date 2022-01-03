# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
____ collections _______ deque


c_ Solution(object):
  ___ - ):
    rBuf = deque([])

  ___ read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    cnt = 0
    tmp = [""] * 4
    w.... cnt < n:
      r = read4(tmp)
      ___ i __ r..(r):
        rBuf.a..(tmp[i])
      ___ i __ r..(m..(n - cnt, l..(rBuf))):
        buf[cnt] = rBuf.popleft()
        cnt += 1
      __ r __ 0:
        break
    r.. cnt
