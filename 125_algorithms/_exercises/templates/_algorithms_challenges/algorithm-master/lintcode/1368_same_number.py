c_ Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    ___ sameNumber  nums, k):
        RES = ('NO', 'YES')

        __ n.. nums o. n.. k:
            r.. RES[0]

        idx    # dict
        gotcha = F..

        ___ i __ r..(l..(nums)):
            __ nums[i] __ idx a.. i - idx[nums[i]] < k:
                gotcha = T..

            idx[nums[i]] = i

        r.. RES[i..(gotcha)]
