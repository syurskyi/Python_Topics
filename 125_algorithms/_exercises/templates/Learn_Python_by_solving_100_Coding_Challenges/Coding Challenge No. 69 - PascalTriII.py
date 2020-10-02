# Pascal's Triangle II
# Question: Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3, Return [1,3,3,1].
# Note: Could you optimize your algorithm to use only O(k) extra space?
# Solutions:


c_ Solution:
    # @return a list of integers
    ___ getRow , rowIndex:
        __ rowIndex __ 0:
            r_ [1]
        __ rowIndex __ 1:
            r_ [1, 1]
        result _ [1]
        nextDivisor _ 1
        nextMultiplier _ rowIndex
        ___ _ __ ra.. rowIndex // 2:
            nextVal _ in.((result[-1] * nextMultiplier / nextDivisor
            result.ap.. nextVal
            nextDivisor +_ 1
            nextMultiplier -_ 1
        __ rowIndex % 2 __ 1:
            result.extend result[::-1]
        ____
            result.extend result[-2::-1]
        r_ result


Solution .getRow 3