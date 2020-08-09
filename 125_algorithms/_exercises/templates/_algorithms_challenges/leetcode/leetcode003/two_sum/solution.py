class Solution:
    # @return a tuple, (index1, index2)
    ___ twoSum(self, num, target
        d = {}
        ___ i, e in enumerate(num
            __ e in d:
                r_ d[e] + 1, i + 1
            d[target - e] = i
