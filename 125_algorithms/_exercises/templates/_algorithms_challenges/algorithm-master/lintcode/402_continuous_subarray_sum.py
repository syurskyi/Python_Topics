c_ Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    ___ continuousSubarraySum  A
        ans [-1, -1]
        __ n.. A:
            r.. ans

        left right 0
        _max _sum f__('-inf')
        ___ i __ r..(l..(A:
            __ _sum < 0:
                _sum A[i]
                left right i
            ____
                _sum += A[i]
                right i

            __ _sum > _max:
                _max _sum
                ans [left, right]

        r.. ans
