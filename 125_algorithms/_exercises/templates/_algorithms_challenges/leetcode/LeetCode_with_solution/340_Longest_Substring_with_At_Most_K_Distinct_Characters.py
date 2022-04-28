c_ Solution o..
    ___ lengthOfLongestSubstringKDistinct  s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = [0] * 256
        i, numDistinct, maxLen = 0, 0, 0
        ___ j __ r.. l.. s)):
            # udpate j
            __ count[o.. s[j])] __ 0:
                numDistinct += 1
            count[o.. s[j])] += 1
            # udpate i
            w.. numDistinct > k:
                count[o.. s[i])] -= 1
                __ count[o.. s[i])] __ 0:
                    numDistinct -= 1
                i += 1
            maxLen =  max(j - i + 1, maxLen)
        r_ maxLen