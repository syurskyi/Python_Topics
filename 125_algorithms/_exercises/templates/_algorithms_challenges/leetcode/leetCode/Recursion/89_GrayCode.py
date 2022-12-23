#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ grayCode  n
        """
        :type n: int
        :rtype: List[int]
        """
        __ n.. n:
            r_ [0]

        __ n __ 1:
            r_ [0, 1]

        # Consume n's sequence is: 0..0, 0..1, ..., 1..0
        # When comes to n+1, it's sequence is simple as followers:
        # 0{0..0, 0..1, ..., 1..0}, 1{1..0, ..., 0..1, 0..0}
        # Then second part of past line is just a reverse of n's sequence.
        high_digit = 2 ** (n-1)
        gray_code_list = self.grayCode(n-1)
        ___ num __ gray_code_list[::-1]:
            gray_code_list.a.. high_digit + num)

        r_ gray_code_list

"""
0
2
3
4
"""
