class Solution(object):
  ___ findComplement(self, num):
    i = 1
    while i <= num:
      i = i << 1
    return (i - 1) ^ num
