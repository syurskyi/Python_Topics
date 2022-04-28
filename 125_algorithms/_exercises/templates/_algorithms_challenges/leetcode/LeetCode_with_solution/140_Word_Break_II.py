c_ Solution o..
    # https://discuss.leetcode.com/topic/12997/11ms-c-solution-concise
    ___ -(self):
        solution  # dict

    ___ wordBreak  s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        try:
            r_ solution[s]
        except KeyError:
            pass
        result = []
        __ s __ wordDict:
            result.append(s)
        ___ i __ r.. 1, l.. s)):
            word = s[i:]
            __ word __ wordDict:
                rem = s[:i]
                prev = wordBreak(rem, wordDict)
                result.extend([res + ' ' + word ___ res __ prev])
        solution[s] = result
        r_ result