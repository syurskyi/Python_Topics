c_ Solution(object):
  ___ nextGreaterElement(self, n):
    """
    :type n: int
    :rtype: int
    """
    num = n
    n = l..(s..(n))
    pos = leftMost = l..(n) - 1
    ___ i __ reversed(r..(0, l..(n) - 1)):
      __ n[i] < n[i + 1]:
        leftMost = i
        break
    ___ i __ reversed(r..(leftMost + 1, l..(n))):
      __ n[i] > n[leftMost]:
        pos = i
        break

    n[leftMost], n[pos] = n[pos], n[leftMost]
    n[leftMost + 1:] = s..(n[leftMost + 1:])
    n = int("".j..(n))
    print
    n
    __ n <= num o. n > 0x7fffffff:
      r.. -1
    r.. n
