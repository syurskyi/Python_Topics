____ c.. _______ n..

Pair = n..('Pair',  'sum', 'index' )

c_ Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    ___ subarraySumClosest  nums
        """
        Prefix Sum
        prefix_sum[i] means the culmulative sum before `i + 1` in `nums`
        => if we want to know the sum of [1, 2]
        => sum(nums[1:3]) == sum(nums[0:3]) - sum(nums[0:0])
        """
        ans = [0] * 2
        __ n.. nums:
            r.. ans

        n = l..(nums)
        __ n __ 1:
            r.. ans

        prefix_sum = [0] * n

        prefix_sum[0] = Pair(nums[0], 0)
        ___ i __ r..(1, n
            prefix_sum[i] = Pair(prefix_sum[i - 1].s.. + nums[i], i)

        # since the closest sum occurred when the sum is closest
        # so we can simply calculate the difference
        # between every two adjacent indexes
        prefix_sum.s..(key=l.... p: p.s..)

        closest_sum = f__('inf')
        tmp_sum = 0
        ___ i __ r..(1, n
            # calculate all the closest sum occurred in two adjacent indexes
            tmp_sum = prefix_sum[i].s.. - prefix_sum[i - 1].s..

            # keep finding the minimum closest sum
            __ tmp_sum >= closest_sum:
                _____

            closest_sum = tmp_sum
            ans = s..([prefix_sum[i].index, prefix_sum[i - 1].index])

        # sum(nums[1:3]) == sum(nums[0:3]) - sum(nums[0:0])
        # so start need `+1`
        ans[0] += 1
        r.. ans
