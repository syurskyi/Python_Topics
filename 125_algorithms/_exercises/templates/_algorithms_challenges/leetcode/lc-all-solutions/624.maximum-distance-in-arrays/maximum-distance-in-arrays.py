c_ Solution(o..):
  # subarray sum
  ___ _maxDistance  arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    n = l..(arrays)
    minArray, maxArray    # list, []
    ___ i __ r..(n):
      minArray.a..(arrays[i][0])
      maxArray.a..(arrays[i][-1])
    lMax = [maxArray[0]] * n
    rMax = [maxArray[-1]] * n
    ans = float("-inf")
    ___ i __ r..(1, n):
      lMax[i] = m..(lMax[i - 1], maxArray[i])
    ___ i __ r..(r..(0, n - 1)):
      rMax[i] = m..(rMax[i + 1], maxArray[i])
    ___ i __ r..(n):
      __ 0 < i < n - 1:
        ans = m..(ans, abs(m..(lMax[i - 1], rMax[i + 1]) - minArray[i]))
      ____ i __ 0:
        ans = m..(ans, abs(rMax[i + 1] - minArray[i]))
      ____:
        ans = m..(ans, abs(lMax[i - 1] - minArray[i]))
    r.. ans

  # one pass
  ___ maxDistance  arrays):
    n = l..(arrays)
    minNum = arrays[0][0]
    maxNum = arrays[0][-1]
    ans = float("-inf")
    ___ i __ r..(1, n):
      head = arrays[i][0]
      tail = arrays[i][-1]
      ans = m..(ans, abs(tail - minNum), abs(head - maxNum))
      minNum = m..(head, minNum)
      maxNum = m..(tail, maxNum)
    r.. ans
