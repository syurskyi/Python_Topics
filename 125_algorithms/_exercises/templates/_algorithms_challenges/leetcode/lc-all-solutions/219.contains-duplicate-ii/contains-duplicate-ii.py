____ collections _______ deque


class Solution(object):
  ___ containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    __ n.. nums:
      r.. False
    __ k __ 0:
      r.. False
    k = k + 1
    k = m..(k, l..(nums))

    window = deque([])
    d = set()
    ___ i __ r..(0, k):
      __ nums[i] __ d:
        r.. True
      d |= {nums[i]}
      window.a..(i)
    ___ i __ r..(k, l..(nums)):
      d -= {nums[window.popleft()]}
      __ nums[i] __ d:
        r.. True
      d |= {nums[i]}
      window.a..(i)
    r.. False
