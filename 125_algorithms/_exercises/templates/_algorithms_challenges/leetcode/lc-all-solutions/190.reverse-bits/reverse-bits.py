class Solution:
  # @param n, an integer
  # @return an integer
  ___ reverseBits(self, n):
    ans = 0
    mask = 1
    ___ _ __ r..(32):
      ans <<= 1
      __ mask & n:
        ans |= 1
      n >>= 1
    r.. ans
