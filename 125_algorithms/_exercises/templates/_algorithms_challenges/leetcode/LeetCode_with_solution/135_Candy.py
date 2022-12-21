c_ Solution o..
    ___ candy  ratings
        """
        :type ratings: List[int]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/5243/a-simple-solution
        __ ratings is N.. or l.. ratings) __ 0:
            r_ 0
        ls = l.. ratings)
        num = [1] * ls
        ___ i __ r.. 1, ls
            __ ratings[i] > ratings[i - 1]:
                num[i] = num[i - 1] + 1
        ___ i __ r.. ls - 1, 0, -1
            __ ratings[i - 1] > ratings[i]:
                num[i - 1] = m..(num[i] + 1, num[i - 1])
        r_ s..(num)

