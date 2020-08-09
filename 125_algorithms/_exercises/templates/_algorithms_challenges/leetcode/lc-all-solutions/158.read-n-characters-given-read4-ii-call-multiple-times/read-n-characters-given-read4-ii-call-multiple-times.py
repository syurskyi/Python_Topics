# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# ___ read4(buf
from collections ______ deque


class Solution(object
  ___ __init__(self
    self.rBuf = deque([])

  ___ read(self, buf, n
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    cnt = 0
    tmp = [""] * 4
    w___ cnt < n:
      r = read4(tmp)
      for i in range(r
        self.rBuf.append(tmp[i])
      for i in range(min(n - cnt, le.(self.rBuf))):
        buf[cnt] = self.rBuf.popleft()
        cnt += 1
      __ r __ 0:
        break
    r_ cnt
