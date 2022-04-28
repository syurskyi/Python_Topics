c_ Solution o..
    ___ subarraySum  nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_map  # dict
        sum_map[0] = 1
        count = curr_sum = 0
        ___ num __ nums:
            curr_sum += num
            # Check if sum - k in hash
            count += sum_map.get(curr_sum - k, 0)
            # add curr_sum to hash
            sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
        r_ count
