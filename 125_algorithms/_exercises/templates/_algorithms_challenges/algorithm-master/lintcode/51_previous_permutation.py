"""
Main Concept:

1. from end to start, finding first increasing element,
   which is `nums[i]`
2. from end to start, finding first element just smaller than `nums[i]`,
   which is `nums[j]`.
   and swap `nums[i]` and `nums[j]`.
3. reverse the elements between `nums[i + 1]` and `nums[n - 1]`

REF: [Next Permutation](https://leetcode.com/articles/next-permutation/)
"""


c_ Solution:
    ___ previousPermuation  nums
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        __ n.. nums o. l..(nums) < 2:
            r.. nums

        n l..(nums)
        i n - 2
        w.... i >_ 0 a.. nums[i] <_ nums[i + 1]:
            i -_ 1

        __ i >_ 0:
            j n - 1
            w.... i < j a.. nums[i] <_ nums[j]:
                j -_ 1
            nums[i], nums[j] nums[j], nums[i]

        i i + 1
        j n - 1
        w.... i < j:
            nums[i], nums[j] nums[j], nums[i]
            i += 1
            j -_ 1

        r.. nums
