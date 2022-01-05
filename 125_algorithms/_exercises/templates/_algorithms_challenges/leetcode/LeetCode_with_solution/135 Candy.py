"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
__author__ = 'Danyang'
c_ Solution:
    ___ candy  ratings):
        """
        dp & re-adjustment

        algorithm: bit.ly/1sod4QC
        2 situations need to be considered
        1. fall below 1
        2. not fall sufficiently

        Wave crest
        Wave trough
        :param ratings: a list of int
        :return: int
        """
        length = l..(ratings)
        dp = [-1 ___ _ __ xrange(length)]
        dp[0] = 1
        ___ ind __ xrange(1, length):
            val = ratings[ind]
            __ ratings[ind-1]<val:
                dp[ind] = dp[ind-1]+1
            ____ ratings[ind-1]>val:
                dp[ind] = dp[ind-1]-1
            ____:
                dp[ind] = 1

            # trough in the middle
            __ ind+1<length a.. ratings[ind-1]>val a.. val<=ratings[ind+1]:
                re_adjust(ratings, dp, ind)

        # trough at the end
        __ ratings[length-2]>ratings[length-1]:
            re_adjust(ratings, dp, length-1)

        r.. s..(dp)

    ___ re_adjust  ratings, dp, ind):
        # backward adjust
        original = dp[ind]
        __ original__1: r..  # no adjustment needed
        i = ind
        candy = 1
        w.... i>0 a.. ratings[i-1]>ratings[i]:  # test case [8, 7, 6, 5, 4, 3, 2, 1]
            dp[i] = candy
            candy += 1
            i -= 1
        # peak
        __ original<1:  # test case [4, 2, 3, 4, 1]
            dp[i] = candy

__ _____ __ ____
    ... Solution().candy([58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89])__208
    ... Solution().candy([4, 2, 3, 4, 1])__9
    ... Solution().candy([1, 4, 3, 2, 1])__11
    ... Solution().candy([8, 7, 6, 5, 4, 3, 2, 1])__36
