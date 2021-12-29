class Solution(object):
  ___ findIntegers(self, num):
    """
    :type num: int
    :rtype: int
    """
    n = bin(num)[2:][::-1]  # removes "0b"
    length = len(n)
    A = [1 for _ in range(length)]  # ends with 0
    B = [1 for _ in range(length)]  # ends with 1

    for i in range(1, len(n)):
      A[i] = A[i - 1] + B[i - 1]
      B[i] = A[i - 1]
    ans = A[-1] + B[-1]
    for i in range(length - 2, -1, -1):
      __ n[i:i + 2] == "11":
        break
      __ n[i:i + 2] == "00":
        ans -= B[i]
    return ans
