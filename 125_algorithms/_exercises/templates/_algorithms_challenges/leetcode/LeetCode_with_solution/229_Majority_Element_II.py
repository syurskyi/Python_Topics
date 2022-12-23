c_ Solution o..
    ___ majorityElement  nums
        # O(1) space
        ls = l.. nums)
        res =    # list
        check_value =    # list
        ___ i __ r.. ls
            __ nums[i] __ check_value:
                c_
            count = 1
            ___ j __ r.. i + 1, ls
                __ nums[i] __ nums[j]:
                    count += 1
            __ count > ls / 3:
                res.a.. nums[i])
            check_value.a.. nums[i])
        r_ res

    # def majorityElement(self, nums):
    #     # using dict
    #     count_hash = {}
    #     res = []
    #     for i in nums:
    #         try:
    #             count_hash[i] += 1
    #         except KeyError:
    #             count_hash[i] = 1
    #     for k, v in count_hash.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res

    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     #https://leetcode.com/discuss/76542/easy-python-solution
    #     tmp = {}
    #     res = []
    #     for n in list(set(nums)):
    #         tmp[n] = nums.count(n)
    #     for k, v in tmp.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res