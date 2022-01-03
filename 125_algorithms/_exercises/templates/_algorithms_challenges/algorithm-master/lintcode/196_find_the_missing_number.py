c_ Solution:
    ___ findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        ans = n = l..(nums)

        ___ i __ r..(n):
            ans ^= i ^ nums[i]

        r.. ans


c_ Solution:
    ___ findMissing(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        __ n.. nums:
            r.. 0

        nums.s..()

        ___ i __ r..(l..(nums)):
            __ i != nums[i]:
                r.. i

        r.. i + 1
