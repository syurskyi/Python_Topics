c_ Solution:
    """
    @param D: the n strings
    @param target: the target string
    @return: The ans
    """
    ___ theLongestCommonPrefix  D, target
        ans 0

        ___ word __ D:
            i 0
            ___ c __ word:
                __ c != target[i]:
                    _____
                i += 1
            __ i > ans:
                ans i

        r.. ans
