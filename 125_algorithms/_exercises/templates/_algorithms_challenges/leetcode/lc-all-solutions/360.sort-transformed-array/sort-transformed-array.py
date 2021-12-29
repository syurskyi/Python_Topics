class Solution(object):
  ___ sortTransformedArray(self, nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """

    ___ f(x):
      return a * (x ** 2) + b * x + c

    __ a == 0:
      __ b >= 0:
        return [f(x) for x in nums]
      else:
        return [f(x) for x in reversed(nums)]

    mid = (-1.0) * b / (2.0 * a)
    up, down = [], []

    __ a >= 0:
      for num in nums:
        __ num >= mid:
          up.append(f(num))
        else:
          down.append(f(num))
      down.reverse()
    else:
      for num in nums:
        __ num >= mid:
          down.append(f(num))
        else:
          up.append(f(num))
      down.reverse()

    res = []
    upIdx = 0
    downIdx = 0
    while upIdx < len(up) and downIdx < len(down):
      upTop = up[upIdx]
      downTop = down[downIdx]

      __ upTop < downTop:
        res.append(upTop)
        upIdx += 1
      else:
        res.append(downTop)
        downIdx += 1
    __ upIdx < len(up):
      res.extend(up[upIdx:len(up)])
    __ downIdx < len(down):
      res.extend(down[downIdx:len(down)])
    return res
