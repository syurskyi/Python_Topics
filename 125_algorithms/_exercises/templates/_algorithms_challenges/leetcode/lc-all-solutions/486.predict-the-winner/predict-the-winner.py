class Solution(object
  ___ PredictTheWinner(self, nums
    """
    :type nums: List[int]
    :rtype: bool
    """

    ___ canWin(nums, start, end, visited, partSum, maxSum, order
      # print "canWin order=", order
      __ (start, end, partSum, order) in visited:
        r_ visited[start, end, partSum, order]
      __ start > end:
        # print "order=", order, partSum, maxSum
        __ order __ 0:
          __ partSum >= maxSum - partSum:
            r_ False
          r_ True
        ____
          __ partSum >= maxSum - partSum:
            r_ True
          r_ False

      visited[start, end, partSum, order] = False
      __ not canWin(nums, start + 1, end, visited, partSum - order * nums[start], maxSum, ~order
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        r_ True
      __ not canWin(nums, start, end - 1, visited, partSum - order * nums[end], maxSum, ~order
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        r_ True
      r_ visited[start, end, partSum, order]

    r_ canWin(nums, 0, le.(nums) - 1, {}, 0, su.(nums), -1)
