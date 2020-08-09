class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    ___ sameNumber(self, nums, k
        RES = ('NO', 'YES')

        __ not nums or not k:
            r_ RES[0]

        idx = {}
        gotcha = False

        ___ i in range(le.(nums)):
            __ nums[i] in idx and i - idx[nums[i]] < k:
                gotcha = True

            idx[nums[i]] = i

        r_ RES[int(gotcha)]
