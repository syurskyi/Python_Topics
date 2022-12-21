#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ fractionToDecimal  numerator, denominator
        # Calcluate the abs's decimal and then add the symbol
        negative = 0
        __ numerator * denominator < 0:
            negative = 1
        numerator, denominator = abs(numerator), abs(denominator)

        answer   # list
        answer.append(str(numerator/denominator))
        remainder = numerator % denominator
        __ remainder:
            answer.append(".")
        # Keep the start position of the repeating part
        remainder_start _ # dict
        _____ remainder:
            remainder *= 10
            __ remainder __ remainder_start:
                answer.insert(remainder_start[remainder], "(")
                answer.append(")")
                ______
            ____
                remainder_start[remainder] = l..(answer)
                answer.append(str(remainder/denominator))
                remainder = remainder % denominator
        __ negative:
            answer.insert(0, "-")
            r_ "".join(answer)
        ____
            r_ "".join(answer)

"""
1
9
-1
999
2
2
-50
-8
-50
8
"""
