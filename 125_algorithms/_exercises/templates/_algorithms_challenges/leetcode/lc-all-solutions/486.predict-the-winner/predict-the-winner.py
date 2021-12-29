class Solution(object):
  ___ PredictTheWinner(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    ___ canWin(nums, start, end, visited, partSum, maxSum, order):
      # print "canWin order=", order
      __ (start, end, partSum, order) in visited:
        return visited[start, end, partSum, order]
      __ start > end:
        # print "order=", order, partSum, maxSum
        __ order == 0:
          __ partSum >= maxSum - partSum:
            return False
          return True
        else:
          __ partSum >= maxSum - partSum:
            return True
          return False

      visited[start, end, partSum, order] = False
      __ not canWin(nums, start + 1, end, visited, partSum - order * nums[start], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        return True
      __ not canWin(nums, start, end - 1, visited, partSum - order * nums[end], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        return True
      return visited[start, end, partSum, order]

    return canWin(nums, 0, len(nums) - 1, {}, 0, sum(nums), -1)
