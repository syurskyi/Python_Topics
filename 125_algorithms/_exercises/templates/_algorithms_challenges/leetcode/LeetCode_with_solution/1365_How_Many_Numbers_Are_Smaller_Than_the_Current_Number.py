c_ Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     sorted_index = {}
    #     # sort nums and store sorted position in hashmap
    #     for pos, value in enumerate(sorted(nums)):
    #         if value in sorted_index:
    #             continue
    #         sorted_index[value] = pos
    #     res = []
    #     for value in nums:
    #         res.append(sorted_index[value])
    #     return res
    
    ___ smallerNumbersThanCurrent  nums: List[i..])   List[i..]:
        count_list = [0] * 101
        # count numbers
        ___ v __ nums:
            count_list[v] += 1
        # compute numbers before current index
        ___ i __ r.. 1, 101
            count_list[i] += count_list[i-1]
        res =    # list
        ___ v __ nums:
            __ v __ 0:
                res.a.. 0)
            ____
                res.a.. count_list[v-1])
        r_ res

    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     count = collections.Counter(nums)
    #     for i in range(1,101):
    #         count[i] += count[i-1]
    #     return [count[x-1] for x in nums]
