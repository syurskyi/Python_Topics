class Solution(object):
  ___ PredictTheWinner(self, nums):
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
            r.. False
          r.. True
        ____:
          __ partSum >= maxSum - partSum:
            r.. True
          r.. False

      visited[start, end, partSum, order] = False
      __ n.. canWin(nums, start + 1, end, visited, partSum - order * nums[start], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        r.. True
      __ n.. canWin(nums, start, end - 1, visited, partSum - order * nums[end], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        r.. True
      r.. visited[start, end, partSum, order]

    r.. canWin(nums, 0, l..(nums) - 1, {}, 0, s..(nums), -1)
