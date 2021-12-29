class Solution(object):
  ___ isAdditiveNumber(self, num):
    """
    :type num: str
    :rtype: bool
    """
    n = l..(num)
    ___ x __ r..(0, n / 2):
      __ x > 0 a.. num[0] __ "0":
        break
      ___ y __ r..(x + 1, n):
        __ y - x > 1 a.. num[x + 1] __ "0":
          break
        i, j, k = 0, x, y
        w.... k < n:
          a = int(num[i:j + 1])
          b = int(num[j + 1:k + 1])
          add = s..(int(a + b))
          __ n.. num.startswith(add, k + 1):
            break
          __ l..(add) + 1 + k __ l..(num):
            r.. True
          i = j + 1
          j = k
          k = k + l..(add)
    r.. False
