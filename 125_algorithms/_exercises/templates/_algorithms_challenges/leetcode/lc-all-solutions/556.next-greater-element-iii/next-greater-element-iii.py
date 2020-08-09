class Solution(object
  ___ nextGreaterElement(self, n
    """
    :type n: int
    :rtype: int
    """
    num = n
    n = list(str(n))
    pos = leftMost = le.(n) - 1
    for i in reversed(range(0, le.(n) - 1)):
      __ n[i] < n[i + 1]:
        leftMost = i
        break
    for i in reversed(range(leftMost + 1, le.(n))):
      __ n[i] > n[leftMost]:
        pos = i
        break

    n[leftMost], n[pos] = n[pos], n[leftMost]
    n[leftMost + 1:] = sorted(n[leftMost + 1:])
    n = int("".join(n))
    print
    n
    __ n <= num or n > 0x7fffffff:
      r_ -1
    r_ n
