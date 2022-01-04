____ r__ _______ randrange


c_ Solution:
    ___ - , nums):
        """
        :type nums: List[int]
        """
        origin = nums |
        nums = nums

    ___ reset
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        nums = origin |
        r.. nums

    ___ shuffle
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        a = nums
        n = l..(a)

        ___ i __ r..(n):
            _i = randrange(i, n)
            a[i], a[_i] = a[_i], a[i]

        r.. a


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
