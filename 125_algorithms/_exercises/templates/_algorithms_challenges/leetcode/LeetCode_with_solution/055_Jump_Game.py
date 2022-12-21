c_ Solution o..
    ___ canJump  nums
        """
        :type nums: List[int]
        :rtype: bool
        """
        # greedy
        # https://leetcode.com/articles/jump-game/
        length = l.. nums)
        begin = length - 1
        ___ i __ reversed(r.. length - 1)):
            __ i + nums[i] >= begin:
                begin = i
        r_ n.. begin