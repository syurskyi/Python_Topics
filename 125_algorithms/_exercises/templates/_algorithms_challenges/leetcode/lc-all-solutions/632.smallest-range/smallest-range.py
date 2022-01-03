____ collections _______ deque


c_ Solution(object):
  ___ smallestRange(self, nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    k = l..(nums)
    d = collections.defaultdict(int)
    tuples    # list

    ___ i __ r..(l..(nums)):
      ___ num __ nums[i]:
        tuples.a..((num, i))

    tuples.s..()
    length = l..(tuples)
    left = tuples[0][0]
    right = tuples[-1][0]
    deq = deque([])
    ___ i __ r..(length):
      num, no = tuples[i]
      deq.a..(tuples[i])
      d[no] += 1
      w.... l..(deq) > 1 a.. d[deq[0][1]] > 1:
        _num, _no = deq.popleft()
        d[_no] -= 1
        __ d[_no] __ 0:
          del d[_no]
      __ l..(d) __ k:
        l, r = deq[0][0], deq[-1][0]
        __ r - l < right - left:
          left = l
          right = r
    r.. (left, right)
