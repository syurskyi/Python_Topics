#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    """ As long as there is a price gap, we gain a profit.
    """
    ___ maxProfit  prices
        max_profit = 0
        ___ i __ r..(1, l..(prices)):
            diff = prices[i] - prices[i - 1]
            __ diff > 0:
                max_profit += diff
        r_ max_profit

"""
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
"""
