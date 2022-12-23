c_ Solution o..
    ___ partition  s
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # https://discuss.leetcode.com/topic/6186/java-backtracking-solution/2
        result =    # list
        curr =    # list
        recurPartition(result, curr, s, 0)
        r_ result

    ___ recurPartition  result, curr, s, start
        __ start __ l.. s
            result.a.. list(curr))
        ___ i __ r.. start, l.. s)):
            __ isPalindrome(s, start, i
                curr.a.. s[start:i + 1])
                recurPartition(result, curr, s, i + 1)
                curr.pop()

    ___ isPalindrome  s, begin, end
        w.. begin < end:
            __ s[begin] != s[end]:
                r_ F..
            begin += 1
            end -= 1
        r_ T..