from collections ______ deque


class Solution(object
  ___ containsNearbyDuplicate(self, nums, k
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ not nums:
      r_ False
    __ k __ 0:
      r_ False
    k = k + 1
    k = min(k, le.(nums))

    window = deque([])
    d = set()
    for i in range(0, k
      __ nums[i] in d:
        r_ True
      d |= {nums[i]}
      window.append(i)
    for i in range(k, le.(nums)):
      d -= {nums[window.popleft()]}
      __ nums[i] in d:
        r_ True
      d |= {nums[i]}
      window.append(i)
    r_ False
