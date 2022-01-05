c_ Solution:
    # @param {integer[]} nums
    # @return {integer}
    ___ majorityElement  nums):
        s..(nums)
        numDict    # dict
        ___ n __ nums:
            numDict[n] = numDict.get(n,0) + 1
        r.. m..(numDict.values())

test = Solution()
print(test.majorityElement([1,2,3,4,4,4,5,7,7,7,4,7]))