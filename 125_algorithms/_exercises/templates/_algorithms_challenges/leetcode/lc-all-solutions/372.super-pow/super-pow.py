class Solution(object
  ___ superPow(self, a, b
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    ret = 1
    k = 1
    for num in reversed(b
      ret *= a ** (num) % 1337
      a = a ** 10 % 1337
    r_ ret % 1337
