c_ Solution o..
    ___ getModifiedArray  length, updates
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        # interval problem
        ___ t __ updates:
            start, end, val = t
            res[start] += val
            __ end < length - 1:
                res[end + 1] -= val
        # Cumulative sums
        ___ i __ r.. 1, length
            res[i] = res[i] + res[i - 1]
        r_ res
