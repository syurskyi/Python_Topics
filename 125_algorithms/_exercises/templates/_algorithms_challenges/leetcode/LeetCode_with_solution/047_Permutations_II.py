c_ Solution o..
    # def __init__(self):
    #     self.result = {}
    #
    # def permuteUnique(self, num):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #         """
    #     if num is None:
    #         return []
    #     num.sort()
    #     self.getPermute([], num)
    #     return self.result.values()
    #
    # def getPermute(self, prefix, rest):
    #     ls = len(rest)
    #     if ls == 0:
    #         return
    #     elif ls == 1:
    #         temp = prefix + rest
    #         stemp = ''.join(str(t) for t in temp)
    #         self.result[stemp] = temp
    #     else:
    #         for i in range(ls):
    #             if i + 1 < ls and rest[i] == rest[i + 1]:
    #                 continue
    #             temp = prefix[:]
    #             temp.append(rest[i])
    #             self.getPermute(temp, rest[:i] + rest[i + 1:])

    ___ permuteUnique  num
        res =    # list
        __ l.. num) __ 0:
            r_ res
        permute(res, num, 0)
        r_ res

    ___ permute  res, num, index
        __ index __ l.. num
            res.a.. list(num))
            r_
        appeared = s..()
        ___ i __ r.. index, l.. num)):
            __ num[i] __ appeared:
                c_
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]

    ___ permuteUnique  num
        # iterative solution
        res = [[]]
        ___ i __ r.. l.. nums)):
            cache = s..()
            w.. l.. res[0]) __ i:
                curr = res.pop(0)
                ___ j __ r.. l.. curr) + 1
                    # generate new n permutations from n -1 permutations
                    new_perm = curr[:j] + [nums[i]] + curr[j:]
                    stemp = ''.join(map(s.., new_perm))
                    __ stemp n.. __ cache:
                        cache.add(stemp)
                        res.a.. new_perm)
        r_ res

