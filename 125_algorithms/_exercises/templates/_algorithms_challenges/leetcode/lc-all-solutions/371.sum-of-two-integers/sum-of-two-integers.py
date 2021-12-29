class Solution(object):
  ___ getSum(self, num1, num2):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    ans = 0
    mask = 0x01
    carry = 0
    for i in range(0, 32):
      a = num1 & mask
      b = num2 & mask
      c = carry
      carry = 0
      __ a ^ b != 0:
        __ c == 1:
          carry = 1
        else:
          ans |= mask
      else:
        __ a & mask > 0:
          carry = 1
        __ c == 1:
          ans |= mask

      mask = mask << 1
    __ ans > 0x7fffffff:
      return ans - 0xffffffff - 1
    return ans
