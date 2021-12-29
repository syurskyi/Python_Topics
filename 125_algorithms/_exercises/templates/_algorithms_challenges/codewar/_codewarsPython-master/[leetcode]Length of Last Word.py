class Solution:
    # @param {string} s
    # @return {integer}
    ___ lengthOfLastWord(self, s):
        num = 0
        s = s.strip()
        for c in s[::-1]:
            __ c == ' ':
                break
            num += 1
        return num

test = Solution()
print(test.lengthOfLastWord('H '))