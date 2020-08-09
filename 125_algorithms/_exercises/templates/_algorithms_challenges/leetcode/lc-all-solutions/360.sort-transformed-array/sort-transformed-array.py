class Solution(object
  ___ sortTransformedArray(self, nums, a, b, c
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """

    ___ f(x
      r_ a * (x ** 2) + b * x + c

    __ a __ 0:
      __ b >= 0:
        r_ [f(x) for x in nums]
      ____
        r_ [f(x) for x in reversed(nums)]

    mid = (-1.0) * b / (2.0 * a)
    up, down = [], []

    __ a >= 0:
      for num in nums:
        __ num >= mid:
          up.append(f(num))
        ____
          down.append(f(num))
      down.reverse()
    ____
      for num in nums:
        __ num >= mid:
          down.append(f(num))
        ____
          up.append(f(num))
      down.reverse()

    res = []
    upIdx = 0
    downIdx = 0
    w___ upIdx < le.(up) and downIdx < le.(down
      upTop = up[upIdx]
      downTop = down[downIdx]

      __ upTop < downTop:
        res.append(upTop)
        upIdx += 1
      ____
        res.append(downTop)
        downIdx += 1
    __ upIdx < le.(up
      res.extend(up[upIdx:le.(up)])
    __ downIdx < le.(down
      res.extend(down[downIdx:le.(down)])
    r_ res
