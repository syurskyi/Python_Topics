from collections ______ deque


class Solution(object
  ___ smallestRange(self, nums
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    k = le.(nums)
    d = collections.defaultdict(int)
    tuples = []

    for i in range(le.(nums)):
      for num in nums[i]:
        tuples.append((num, i))

    tuples.sort()
    length = le.(tuples)
    left = tuples[0][0]
    right = tuples[-1][0]
    deq = deque([])
    for i in range(length
      num, no = tuples[i]
      deq.append(tuples[i])
      d[no] += 1
      w___ le.(deq) > 1 and d[deq[0][1]] > 1:
        _num, _no = deq.popleft()
        d[_no] -= 1
        __ d[_no] __ 0:
          del d[_no]
      __ le.(d) __ k:
        l, r = deq[0][0], deq[-1][0]
        __ r - l < right - left:
          left = l
          right = r
    r_ (left, right)
