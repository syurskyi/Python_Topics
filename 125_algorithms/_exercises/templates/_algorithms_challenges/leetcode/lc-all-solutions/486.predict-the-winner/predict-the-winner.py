c_ Solution(o..):
  ___ PredictTheWinner  nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    ___ canWin(nums, start, end, visited, partSum, maxSum, order):
      # print "canWin order=", order
      __ (start, end, partSum, order) __ visited:
        r.. visited[start, end, partSum, order]
      __ start > end:
        # print "order=", order, partSum, maxSum
        __ order __ 0:
          __ partSum >= maxSum - partSum:
            r.. F..
          r.. T..
        ____:
          __ partSum >= maxSum - partSum:
            r.. T..
          r.. F..

      visited[start, end, partSum, order] = F..
      __ n.. canWin(nums, start + 1, end, visited, partSum - order * nums[start], maxSum, ~order):
        visited[start, end, partSum, order] = T..
        # print "order=", order, "return True"
        r.. T..
      __ n.. canWin(nums, start, end - 1, visited, partSum - order * nums[end], maxSum, ~order):
        visited[start, end, partSum, order] = T..
        # print "order=", order, "return True"
        r.. T..
      r.. visited[start, end, partSum, order]

    r.. canWin(nums, 0, l..(nums) - 1, {}, 0, s..(nums), -1)
