c_ Solution(o..
  ___ findUnsortedSubarray  nums
    """
    :type nums: List[int]
    :rtype: int
    """
    __ l..(nums) < 2:
      r.. 0
    maxs = [f__("inf")] * l..(nums)
    mins = [f__("inf")] * l..(nums)
    mins[-1] = nums[-1]
    maxs[0] = nums[0]
    start, end = 0, -2
    ___ i __ r..(1, l..(nums)):
      maxs[i] = m..(maxs[i - 1], nums[i])
    ___ i __ r..(r..(l..(nums) - 1)):
      mins[i] = m..(mins[i + 1], nums[i])
    ___ i __ r..(r..(1, l..(nums))):
      __ nums[i] < maxs[i - 1]:
        end = i
        _____
    ___ i __ r..(l..(nums) - 1
      __ nums[i] > mins[i + 1]:
        start = i
        _____
    print
    end, start
    r.. m..(end - start + 1, 0)
