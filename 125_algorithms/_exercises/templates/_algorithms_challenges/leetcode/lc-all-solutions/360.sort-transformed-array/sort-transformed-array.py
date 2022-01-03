c_ Solution(object):
  ___ sortTransformedArray(self, nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """

    ___ f(x):
      r.. a * (x ** 2) + b * x + c

    __ a __ 0:
      __ b >= 0:
        r.. [f(x) ___ x __ nums]
      ____:
        r.. [f(x) ___ x __ reversed(nums)]

    mid = (-1.0) * b / (2.0 * a)
    up, down    # list, []

    __ a >= 0:
      ___ num __ nums:
        __ num >= mid:
          up.a..(f(num))
        ____:
          down.a..(f(num))
      down.reverse()
    ____:
      ___ num __ nums:
        __ num >= mid:
          down.a..(f(num))
        ____:
          up.a..(f(num))
      down.reverse()

    res    # list
    upIdx = 0
    downIdx = 0
    w.... upIdx < l..(up) a.. downIdx < l..(down):
      upTop = up[upIdx]
      downTop = down[downIdx]

      __ upTop < downTop:
        res.a..(upTop)
        upIdx += 1
      ____:
        res.a..(downTop)
        downIdx += 1
    __ upIdx < l..(up):
      res.extend(up[upIdx:l..(up)])
    __ downIdx < l..(down):
      res.extend(down[downIdx:l..(down)])
    r.. res
