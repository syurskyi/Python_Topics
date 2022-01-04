"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
_______ r__

__author__ = 'Daniel'


c_ Solution(object):
    ___ - , nums):
        """
        :type nums: List[int]
        :type size: int
        """
        original = nums

    ___ reset
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        r.. l..(original)

    ___ shuffle
        """
        Returns a random shuffling of the array.
        like shuffle the poker cards
        in-place shuffling and avoid dynamic resizing the list
        :rtype: List[int]
        """
        lst = reset()
        n = l..(lst)
        ___ i __ xrange(n):
            j = r__.randrange(i, n)
            lst[i], lst[j] = lst[j], lst[i]

        r.. lst


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()