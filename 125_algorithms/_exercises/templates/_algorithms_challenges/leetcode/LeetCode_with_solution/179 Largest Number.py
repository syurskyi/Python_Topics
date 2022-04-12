"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
__author__ 'Daniel'


c_ Solution:
    ___ largestNumber  nums
        """
        Start off by enumerate simple examples

        Compare digit by digit
        The comparator is the core.

        :type nums: list[int]
        :rtype: str
        """
        nums map(s.., nums)
        nums.s..(cmp=cmp, r.._T..
        nums "".j..(nums)
        nums nums.l..("0")
        __ n.. nums:
            nums "0"
        r.. nums

    ___ cmp  a, b
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        order 1
        __ l..(a) > l..(b
            order -1
            a, b b, a

        ___ i __ x..(l..(a:
            __ i..(a[i]) !_ i..(b[i]
                r.. order*(i..(a[i])-i..(b[i]

        __ l..(a) __ l..(b
            r.. 0

        r.. order*cmp(a, b[l..(a])


__ _______ __ _______
    ... Solution().largestNumber(
        [4704, 6306, 9385, 7536, 3462, 4798, 5422, 5529, 8070, 6241, 9094, 7846, 663, 6221, 216, 6758, 8353, 3650, 3836,
         8183, 3516, 5909, 6744, 1548, 5712, 2281, 3664, 7100, 6698, 7321, 4980, 8937, 3163, 5784, 3298, 9890, 1090,
         7605, 1380, 1147, 1495, 3699, 9448, 5208, 9456, 3846, 3567, 6856, 2000, 3575, 7205, 2697, 5972, 7471, 1763,
         1143, 1417, 6038, 2313, 6554, 9026, 8107, 9827, 7982, 9685, 3905, 8939, 1048, 282, 7423, 6327, 2970, 4453,
         5460, 3399, 9533, 914, 3932, 192, 3084, 6806, 273, 4283, 2060, 5682, 2, 2362, 4812, 7032, 810, 2465, 6511, 213,
         2362, 3021, 2745, 3636, 6265, 1518, 8398]) __ "98909827968595339456944893859149094902689398937839883538183810810780707982784676057536747174237321720571007032685668066758674466986636554651163276306626562416221603859725909578457125682552954605422520849804812479847044453428339323905384638363699366436503636357535673516346233993298316330843021297028227452732697246523622362231322812216213206020001921763154815181495141713801147114310901048"