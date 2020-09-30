# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# ___ read4(buf

class Solution(object
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
      __ r __ 0:
        break
      ___ i __ range(min(r, n - cnt)):
        buf[cnt] = tmp[i]
        cnt += 1
    r_ cnt
