c_ Solution o..
    ___ partition  s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # https://discuss.leetcode.com/topic/6186/java-backtracking-solution/2
        result = []
        curr = []
        recurPartition(result, curr, s, 0)
        r_ result

    ___ recurPartition  result, curr, s, start):
        __ start __ l.. s):
            result.append(list(curr))
        ___ i __ r.. start, l.. s)):
            __ isPalindrome(s, start, i):
                curr.append(s[start:i + 1])
                recurPartition(result, curr, s, i + 1)
                curr.pop()

    ___ isPalindrome  s, begin, end):
        w.. begin < end:
            __ s[begin] != s[end]:
                r_ False
            begin += 1
            end -= 1
        r_ True