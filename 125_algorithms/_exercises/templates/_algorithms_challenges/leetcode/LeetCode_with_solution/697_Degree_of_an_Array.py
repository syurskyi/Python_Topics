c_ Solution o..
    # def findShortestSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     res = len(nums)
    #     counter = collections.Counter()
    #     for num in nums:
    #         counter[num] += 1
    #     degree = max(counter.values())
    #     for key, kdegree in counter.most_common():
    #         if degree != kdegree:
    #             break
    #         res = min(res, self.smallestSubArray(nums, key, degree))
    #     return res

    # def smallestSubArray(self, nums, key, degree):
    #     start = nums.index(key)
    #     pos = start + 1
    #     degree -= 1
    #     while pos < len(nums) and degree != 0:
    #         if nums[pos] == key:
    #             degree -= 1
    #         pos += 1
    #     return pos - start

    ___ findShortestSubArray  nums
        left, right, count  # dict, {}, {}
        ___ i, x __ e.. nums
            __ x n.. __ left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = l.. nums)
        degree = m..(count.values())
        ___ x __ count:
            __ count[x] __ degree:
                ans = m.. ans, right[x] - left[x] + 1)

        r_ ans
