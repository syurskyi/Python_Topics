c_ Solution o..
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # hash
    #     dic = {}
    #     for num in nums:
    #         try:
    #             dic[num] += 1
    #         except KeyError:
    #             dic[num] = 1
    #     for num in nums:
    #         if dic[num] == 1:
    #             return num

    # def singleNumber(self, nums):
    #     # set
    #     s = set()
    #     for num in nums:
    #         if num in s:
    #             s.remove(num)
    #         else:
    #             s.add(num)
    #     return s.pop()

    ___ singleNumber  nums
        # xor
        res = 0
        ___ num __ nums:
            res ^= num
        r_ res