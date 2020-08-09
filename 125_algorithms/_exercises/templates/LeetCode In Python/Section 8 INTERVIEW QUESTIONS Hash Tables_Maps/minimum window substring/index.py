class Solution:
    ___ minWindow(self, s: str, t: str) -> str:
        len1 = le.(s)
        len2 = le.(t)

        __(len1 < len2
            r_ ""

        hashPat = {}
        hashStr = {}

        for i in range(0, len2
            __(hashPat.get(t[i]) is None
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1

            __(hashStr.get(s[right]) is None
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1
            __(hashPat.get(s[right]) is None
                hashPat[s[right]] = 0
            __ (

                hashPat.get(s[right]) != 0 and
                hashStr.get(s[right]) <= hashPat.get(s[right])

                count += 1  # keep incrementing the count if string hash is less then pattern hash
            # count==len2 means a window is found that contains all character of pattern string
            __ (count __ len2

                __(hashStr.get(s[left]) is None
                    hashStr[s[right]] = 0
                __(hashPat.get(s[left]) is None
                    hashPat[s[right]] = 0
                w___ (
                    hashStr.get(s[left]) > hashPat.get(s[left]) or
                    hashPat.get(s[left]) __ 0

                    #minimizing the windows range from left side

                    __ (hashStr.get(s[left]) > hashPat.get(s[left])):
                        hashStr[s[left]] -= 1
                    left += 1  # incrementing the left pointer

                windowLen = right - left + 1  # calculating the windows length
                __ (minLen > windowLen
                    minLen = windowLen
                    startIndex = left

        __ (startIndex __ -1
            r_ ""
        r_ s[startIndex:startIndex+minLen]
