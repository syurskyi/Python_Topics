c_ Solution o..
    ___ generatePalindromes  s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic  # dict
        half =    # list
        res =    # list
        ___ c __ s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        ___ c __ dic:
            __ dic[c] % 2 __ 0:
                even += 1
            ____
                odd += 1
        __ odd > 1:
            r_    # list
        # generate half
        seed =    # list
        mid = ''
        ___ c __ dic:
            __ dic[c] % 2 __ 1:
                mid = c
            seed.extend([c] * (dic[c] / 2))
        permute(half, seed, 0)
        # merge half to get res
        ___ r __ half:
            res.append(''.join(r) + mid + ''.join(reversed(r)))
        r_ res

    ___ permute  res, num, index):
        __ index __ l.. num):
            res.append(list(num))
            r_
        appeared = set()
        ___ i __ r.. index, l.. num)):
            __ num[i] __ appeared:
                continue
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]
