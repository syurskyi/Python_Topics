class Solution(object
  ___ maxSlidingWindow(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    __ k __ 0:
      r_ []
    ans = [0 ___ _ in range(le.(nums) - k + 1)]
    stack = collections.deque([])
    ___ i in range(0, k
      w___ stack and nums[stack[-1]] < nums[i]:
        stack.p..
      stack.append(i)
    ans[0] = nums[stack[0]]
    idx = 0
    ___ i in range(k, le.(nums)):
      idx += 1
      __ stack and stack[0] __ i - k:
        stack.popleft()
      w___ stack and nums[stack[-1]] < nums[i]:
        stack.p..
      stack.append(i)
      ans[idx] = nums[stack[0]]

    r_ ans
