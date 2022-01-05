c_ Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    ___ subarraySum  nums):
        """
        len(nums) == 5
        if `A[1] + A[2] + A[3] == 0`
        the cumulative sum in the `i == 3` iteration
        is same as the cumulative sum in `A[0]`

        => save every sum in hashmap
        => if got the same sum in following iteration
        => start = hashmap[sum] + 1, end = i
        """
        __ n.. nums:
            r.. []

        sum_to_index    # dict
        sum_to_index[0] = -1

        prefix_sum = 0
        ___ i __ r..(l..(nums)):
            prefix_sum += nums[i]

            __ prefix_sum __ sum_to_index:
                r.. [
                    sum_to_index[prefix_sum] + 1,
                    i
                ]

            sum_to_index[prefix_sum] = i

        r.. []
