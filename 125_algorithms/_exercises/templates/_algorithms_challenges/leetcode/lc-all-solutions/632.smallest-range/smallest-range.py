____ c.. _______ d..


c_ Solution(o..
  ___ smallestRange  nums
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    k l..(nums)
    d c...d..(i..)
    tuples    # list

    ___ i __ r..(l..(nums:
      ___ num __ nums[i]:
        tuples.a..((num, i

    tuples.s..()
    length l..(tuples)
    left tuples[0][0]
    right tuples[-1][0]
    deq d..([])
    ___ i __ r..(length
      num, no tuples[i]
      deq.a..(tuples[i])
      d[no] += 1
      w.... l..(deq) > 1 a.. d[deq[0][1]] > 1:
        _num, _no deq.popleft()
        d[_no] -_ 1
        __ d[_no] __ 0:
          del d[_no]
      __ l..(d) __ k:
        l, r deq[0][0], deq[-1][0]
        __ r - l < right - left:
          left l
          right r
    r.. (left, right)
