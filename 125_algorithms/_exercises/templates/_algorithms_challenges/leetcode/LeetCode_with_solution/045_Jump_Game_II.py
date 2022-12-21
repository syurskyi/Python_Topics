c_ Solution:
    ___ jump  nums
        """
        :type nums: List[int]
        :rtype: int
        """
        __ l.. nums) <= 1:
            r_ 0
        end = 0 + nums[0]
        start = 0
        step = 1
        maxDis = 0 + nums[0]
        w.. end < l.. nums) - 1:
            ___ i __ r.. start + 1, end + 1
                # greedy
                maxDis = m..(maxDis, nums[i] + i)
            start = end
            end = maxDis
            step += 1
        r_ step
