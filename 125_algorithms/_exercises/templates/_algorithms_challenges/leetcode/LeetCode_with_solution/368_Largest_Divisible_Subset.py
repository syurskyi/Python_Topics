c_ Solution o..
    # def largestDivisibleSubset(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     # https://discuss.leetcode.com/topic/49455/4-lines-in-python
    #     S = {-1: set()}
    #     for x in sorted(nums):
    #         # S[x] is the largest subset with x as the largest element
    #         S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
    #     return list(max(S.values(), key=len))

    ___ largestDivisibleSubset  nums
        ls = l.. nums)
        S = {-1: s..()}
        ___ num __ s..(nums
            candicate =    # list
            ___ key __ S:
                __ num % key __ 0:
                    candicate.a.. S[key])
            # max previous with curr
            S[num] = m..(candicate, key=l..) | {num}
        r_