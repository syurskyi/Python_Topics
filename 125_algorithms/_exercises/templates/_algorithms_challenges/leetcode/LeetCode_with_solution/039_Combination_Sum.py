c_ Solution o..
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     candidates.sort()
    #     return self.getcombinationSum(candidates, [], 0, target)
    #
    #
    # def getcombinationSum(self, candidates, prefix, curr, target):
    #     if len(prefix) == 0:
    #         max_value = candidates[0]
    #     else:
    #         max_value = prefix[-1]
    #     res = []
    #     for i in range(len(candidates)):
    #         if candidates[i] >= max_value:
    #             if curr + candidates[i] == target:
    #                 res.append(prefix+[candidates[i]])
    #             elif curr + candidates[i] < target:
    #                 res.extend(self.getcombinationSum(candidates, prefix+[candidates[i]], curr + candidates[i], target))
    #             else:
    #                 pass
    #     return res


    ___ combinationSum  candidates, target
        candidates.s..
        dp = [[] ___ _ __ r.. target + 1)]
        dp[0].append(   # list)
        ___ i __ r.. 1, target + 1
            ___ j __ r.. l.. candidates)):
                __ candidates[j] > i:
                    break
                ___ k __ r.. l.. dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    __ l.. temp) > 0 and temp[-1] > candidates[j]:
                        c_
                    temp.append(candidates[j])
                    dp[i].append(temp)
        r_ dp[target]


__ ____ __ ____
    s  ?
    print s.combinationSum([8,7,4,3], 11)




