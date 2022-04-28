c_ Solution o..
    ___ combinationSum2  candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.s..
        dp = [[] ___ _ __ r.. target + 1)]
        dp[0].append([])
        ___ i __ r.. 1, target + 1):
            ___ j __ r.. l.. candidates)):
                __ candidates[j] > i:
                    break
                ___ k __ r.. l.. dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # check if this number is used
                    __ l.. temp) > 0 and temp[-1] >= j:
                        continue
                    # store index
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check  # dict
        ___ temp __ dp[target]:
            value = [candidates[t] ___ t __ temp]
            try:
                check[str(value)] += 1
            except KeyError:
                check[str(value)] = 1
                res.append(value)
        r_ res