import random
c_ Solution o..
    ___ -  nums
        """
        :type nums: List[int]
        :type size: int
        """
        origin = list(nums)
        curr = list(nums)
        size = l.. nums)

    ___ reset ____:
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        curr = list(origin)
        r_ curr

    ___ shuffle ____:
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ___ i __ r.. size
            pos = random.randint(0, i)
            # swap i and pos
            curr[i], curr[pos] = curr[pos], curr[i]
        r_ curr


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()