c_ Solution o..
    ___ combinationSum2  candidates, target
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.s..
        dp = [[] ___ _ __ r.. target + 1)]
        dp[0].a..    # list)
        ___ i __ r.. 1, target + 1
            ___ j __ r.. l.. candidates)):
                __ candidates[j] > i:
                    ______
                ___ k __ r.. l.. dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # check if this number is used
                    __ l.. temp) > 0 a.. temp[-1] >= j:
                        c_
                    # store index
                    temp.a.. j)
                    dp[i].a.. temp)
        res =    # list
        check  # dict
        ___ temp __ dp[target]:
            value = [candidates[t] ___ t __ temp]
            try:
                check[s..(value)] += 1
            except KeyError:
                check[s..(value)] = 1
                res.a.. value)
        r_ res