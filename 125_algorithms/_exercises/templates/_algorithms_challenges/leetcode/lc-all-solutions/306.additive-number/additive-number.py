class Solution(object
  ___ isAdditiveNumber(self, num
    """
    :type num: str
    :rtype: bool
    """
    n = le.(num)
    ___ x in range(0, n / 2
      __ x > 0 and num[0] __ "0":
        break
      ___ y in range(x + 1, n
        __ y - x > 1 and num[x + 1] __ "0":
          break
        i, j, k = 0, x, y
        w___ k < n:
          a = int(num[i:j + 1])
          b = int(num[j + 1:k + 1])
          add = str(int(a + b))
          __ not num.startswith(add, k + 1
            break
          __ le.(add) + 1 + k __ le.(num
            r_ True
          i = j + 1
          j = k
          k = k + le.(add)
    r_ False
